### README: Web-Based Tool for Regulatory Motif Detection and Annotation
### Final-Project
This Tool is the final project for the Advanced Practical computer concepts class. 
---

#### **Project Title**:  
A Web-Based Tool for Regulatory Motif Detection and Annotation  

---

#### **Project Description**:  
This tool is designed to detect regulatory motifs in DNA sequences submitted in FASTA format and annotate them with visual highlights. It provides an efficient solution for motif analysis by summarizing motif occurrences, including their names, positions, and visually marking motifs in the DNA sequences for easy interpretation.

---

#### **Objectives**:
1. **Motif Detection**:  
   - Identify all regulatory motifs stored in a MySQL database within input DNA sequences.  

2. **Sequence Annotation**:  
   - Highlight detected motifs in DNA sequences using distinct colors for easy visualization.  

3. **Summary Output**:  
   - Generate a summary report detailing motif names, start and end positions, motif type and description about the motif.  

---

#### **Key Features**:  
1. **User Input**:  
   - Accepts DNA sequences in FASTA format via a web form.  

2. **Motif Detection**:  
   - Searches for motifs stored in the MySQL database.
   - Outputs motif names, start and end positions, motif type and description about the motif.  

3. **Sequence Annotation**:  
   - Visually highlights motifs directly within the sequence using HTML `<span>` tags with inline styles.  

4. **Summary Report**:  
   - Displays detected motifs, provides thier JASPER ID, position on the sequence (zero-based), and associated sequence headers.  

---

#### **Methodology**:  
1. **Database Design**:  
   A relational database stores motif details with the following schema:  

   | Column Name       | Data Type       | Purpose                                        |
   |-------------------|-----------------|------------------------------------------------|
   | `motif_id`        | `VARCHAR(10)`   | JASPAR ID to uniquely identify each motif.     |
   | `motif_name`      | `VARCHAR(100)`  | Name of the motif (e.g., TBP, TATA Box).       |
   | `sequence_pattern`| `VARCHAR(50)`   | DNA sequence pattern used for motif detection. |
   | `motif_type`      | `VARCHAR(50)`   | Functional type (e.g., promoter, enhancer).    |
   | `description`     | `TEXT`          | Detailed description of motif functionality.   |

   - Database populated with 30 motifs from JASPAR.

2. **Backend Development**:  
   - **FASTA Parsing**: Parse input files to extract headers and sequences.  
   - **Motif Search**: Use regular expressions to locate motifs in sequences.  
   - **Annotation**: Embed highlights using HTML `<span>` tags.  

3. **Frontend Development**:  
   - Web form for uploading FASTA files.  
   - Display annotated sequences and a detailed summary of detected motifs.  

4. **Testing and Validation**:  
   - Validate the tool using known sequences containing expected motifs.  

5. **Deployment**:  
   - Host the tool on a shared class server using Python CGI for dynamic functionality.  

---

#### **Expected Outputs**:  
1. **Highlighted Sequences**:  
   - DNA sequences with visually marked motifs in distinct color.  

2. **Summary Report**:  
   - Comprehensive details on detected motifs, including names, start and end positions, JASPER ID, Descripition of the motif.  

---

#### **Usage Instructions**:
1. **Upload Input**:  
   - Submit DNA sequences in FASTA format using the web interface.  

2. **View Results**:  
   - Annotated sequences with highlighted motifs.  
   - Summary table with motif occurrences and details.  

3. **Download Outputs**:  
   - Save annotated sequences and the summary report for further analysis.  

---

#### **Applications**:  
- Research into gene regulation and transcriptional control.  
- Identification of regulatory elements in DNA sequences.  
- Exploration of transcription factor binding sites and their biological relevance.  

---

#### **Acknowledgments**:  
This project is part of a final coursework submission. Motif data is sourced from JASPAR Database, and the tool is developed using Python, MySQL, CSS, Java script.  
