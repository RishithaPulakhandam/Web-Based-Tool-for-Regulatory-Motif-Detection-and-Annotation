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
        database="rpulakh1"
    )

# Function to parse FASTA input
def parse_fasta(fasta_input):
    sequences = {}
    current_header = None

    if fasta_input:  # FASTA sequence Input
        lines = fasta_input.strip().split("\n")
        for line in lines:
            if line.startswith(">"):  # Header line
                current_header = line[1:].strip()
                sequences[current_header] = ""
            elif current_header:  # Sequence line
                sequences[current_header] += line.strip()
            else:
                raise ValueError("FASTA input is improperly formatted: Missing header.")

    if not sequences: #Error Handling when no sequence is provided
        raise ValueError("No sequences found in the provided FASTA input.")

    return sequences

# Function to retrieve motifs from the database
def get_motifs():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT motif_id, motif_name, sequence_pattern, motif_type, description FROM regulatory_motifs")
    motifs = cursor.fetchall()
    cursor.close()
    db.close()
    return motifs

# Function to annotate a sequence with motifs
def annotate_sequence(sequence, motifs):
    annotated_seq = html.escape(sequence)
    detected_motifs = []

    for motif_id, motif_name, pattern, motif_type, description in motifs:
        for match in re.finditer(pattern, sequence):  # To find all matches of the motif
            start, end = match.start(), match.end()  # To get start and end positions
            description = description.replace(". ", ".<br>")
            detected_motifs.append({
                "motif_id": motif_id,            # JASPER ID
                "motif_name": motif_name,        # Motif Name
                "motif_type": motif_type,        # Motif Type
                "start": start,                  # Position
                "end": end,
                "sequence": match.group(),       # Detected Sequence
                "description": description       # Description
            })
            # Highlight the detected motif in the sequence
            annotated_seq = (
                annotated_seq[:start]
                + f"<span style='color:red;'>{html.escape(annotated_seq[start:end])}</span>"
                + annotated_seq[end:]
            )

    return annotated_seq, detected_motifs

# Main function to handle CGI input and output
def main():
    print("Content-Type: application/json\n")  # HTTP header for JSON response

    form = cgi.FieldStorage()
    fasta_input = form.getfirst("fasta_input", "").strip()  # To get text input

    try:
        # Checking if fasta_input is provided
        if not fasta_input:
            raise ValueError("No FASTA sequence provided.")

        # Parsing the FASTA input
        sequences = parse_fasta(fasta_input)

        # Retrieving the motifs from the database
        motifs = get_motifs()

        # Annotate sequences and collect results
        output = {}
        for header, sequence in sequences.items():
            annotated_seq, detected_motifs = annotate_sequence(sequence, motifs)
            output[header] = {
                "annotated_sequence": annotated_seq,  # Annotated sequence with HTML tags
                "motifs": detected_motifs             # Detected motifs with details in the form of a table
            }

        # Returning the annotated sequences and motif details as JSON
        print(json.dumps(output))

    except ValueError as e:
        print(json.dumps({"error": str(e)}))

    except Exception as e:
        print(json.dumps({"error": "An unexpected error occurred.", "details": str(e)}))

if __name__ == "__main__":
    main()
