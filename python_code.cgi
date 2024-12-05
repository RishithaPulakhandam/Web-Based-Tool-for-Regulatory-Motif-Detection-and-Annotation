#!/usr/bin/env python3

import cgi
import cgitb
import mysql.connector
import re
import json
import html

cgitb.enable()

# Function to connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="rpulakh1",
        password="$@!RAm1006",
        database="motif_detection_tool"
    )

# Function to parse a FASTA file
def parse_fasta(file, fasta_input):
    sequences = {}
    current_header = None  # Initialize header variable

    if fasta_input:  # If a direct input is provided
        lines = fasta_input.strip().split("\n")
        for line in lines:
            if line.startswith(">"):  # Header line
                current_header = line[1:].strip()
                sequences[current_header] = ""
            elif current_header:  # Sequence line
                sequences[current_header] += line.strip()
            else:
                raise ValueError("FASTA input is improperly formatted: Missing header.")

    elif file and file.file:  # If a file is uploaded
        for line in file.file:
            line = line.decode("utf-8").strip()  # Decode to string
            if line.startswith(">"):  # Header line
                current_header = line[1:].strip()
                sequences[current_header] = ""
            elif current_header:  # Sequence line
                sequences[current_header] += line.strip()
            else:
                raise ValueError("FASTA file is improperly formatted: Missing header.")

    else:
        raise ValueError("No input provided for FASTA parsing.")

    if not sequences:
        raise ValueError("No sequences found in the provided FASTA input.")

    return sequences

# Function to retrieve motifs from the database
def get_motifs():
    db = connect_db()  # Connecting to the database
    cursor = db.cursor()
    cursor.execute("SELECT motif_id, motif_name, sequence_pattern FROM regulatory_motifs")
    motifs = cursor.fetchall()  # Fetching all motifs
    cursor.close()
    db.close()
    return motifs

# Function to annotate a sequence with motifs
def annotate_sequence(sequence, motifs):
    """
    Detects motifs in a given sequence and annotates it by wrapping matching motifs
    with HTML tags for highlighting.
    Returns the annotated sequence and a list of detected motifs.
    """
    annotated_seq = sequence  # Start with the unannotated sequence
    detected_motifs = []  # List to store detected motifs

    # Check each motif pattern in the sequence
    for motif_id, motif_name, pattern in motifs:
        for match in re.finditer(pattern, sequence):  # To find all matches of the motif
            start, end = match.start(), match.end()  # Getting start and end positions
            detected_motifs.append({
                "motif_id": motif_id,
                "motif_name": motif_name,
                "start": start,
                "end": end,
                "sequence": match.group()  # The matched motif sequence
            })
            # Highlighting the detected motif in the sequence
            annotated_seq = (
                annotated_seq[:start]
                + f"<span style='color:red;'>{annotated_seq[start:end]}</span>"
                + annotated_seq[end:]
            )
    return annotated_seq, detected_motifs

# Main function to handle CGI input and output
def main():
    # Print the HTTP content-type header for JSON response
    print("Content-Type: application/json\n")

    # Parsing the form data submitted via CGI
    form = cgi.FieldStorage()
    fasta_input = form.getfirst("fasta_input", "").strip()  # Text area input
    fileitem = form["fasta_file"] if "fasta_file" in form else None  # File upload

    try:
        # Parse the FASTA input from either a file or direct text
        sequences = parse_fasta(fileitem, fasta_input)

        # Retrieve motifs from the database
        motifs = get_motifs()

        # Annotate sequences and collect results
        output = {}
        for header, sequence in sequences.items():
            annotated_seq, detected_motifs = annotate_sequence(sequence, motifs)
            output[header] = {
                "annotated_sequence": annotated_seq,  # Annotated sequence with HTML tags
                "motifs": detected_motifs             # Detected motifs with details
            }

        # Return the annotated sequences and motif details as JSON
        print(json.dumps(output))

    except ValueError as e:
        # Handle input validation errors
        print(json.dumps({"error": str(e)}))

    except Exception as e:
        # Handle unexpected errors
        print(json.dumps({"error": "An unexpected error occurred.", "details": str(e)}))

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
