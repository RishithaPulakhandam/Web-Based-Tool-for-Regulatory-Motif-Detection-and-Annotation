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
def parse_fasta(file):
    sequences = {}
    current_header = None
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_header = line[1:]
            sequences[current_header] = ""
        else:
            sequences[current_header] += line
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
    fileitem = form["fasta_file"]

    if fileitem.file:
        sequences = parse_fasta(fileitem.file)  # Parse the uploaded FASTA file
        motifs = get_motifs()  # Retrieve motifs from the database

        output = {}  # Dictionary to store results
        for header, sequence in sequences.items():
            # Annotate sequence and detect motifs
            annotated_seq, detected_motifs = annotate_sequence(sequence, motifs)
            output[header] = {
                "annotated_sequence": annotated_seq,  # Annotated sequence with HTML tags
                "motifs": detected_motifs  # Detected motifs with details
            }

        # Return the output as a JSON response
        print(json.dumps(output))
    else:
        # Handle the case where no file is uploaded
        print(json.dumps({"error": "No file was uploaded"}))

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
