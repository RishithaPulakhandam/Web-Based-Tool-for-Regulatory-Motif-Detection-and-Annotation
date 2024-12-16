// Event listener for form submission
document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const fastaInput = document.getElementById('fasta_input').value.trim(); // To get FASTA text input

    // Validating that the text input is provided
    if (!fastaInput) {
        alert('Please provide a FASTA sequence.');
        return;
    }

    const formData = new FormData();
    formData.append('fasta_input', fastaInput);

    try {
        // Sending the form data to the backend
        const response = await fetch('/rpulakh1/Final-Project/python_code.cgi', {
            method: 'POST',
            body: formData,
        });

        // Checking the response status
        if (!response.ok) {
           throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parsing the JSON response
        const data = await response.json();

        // Display the results
        displayResults(data);
    } catch (error) {
        // Handling errors during the request
        alert('An error occurred while processing your request.');
        console.error('Error:', error);
    }
});

// Function to display the results dynamically
function displayResults(data) {
    const sequenceOutput = document.getElementById('sequenceOutput');
    const resultsSection = document.getElementById('results');
    const summaryTable = document.getElementById('summaryTable');
    const motifSummaryHeading = document.getElementById('motifSummaryHeading');
    const tableBody = summaryTable.querySelector('tbody');
    const noMatchesMessage = document.getElementById('noMatchesMessage');

    sequenceOutput.innerHTML = '';
    tableBody.innerHTML = '';

    noMatchesMessage.style.display = 'none'; // Hiding "No matches" message by default
    summaryTable.style.display = 'none'; // Hiding table by default
    motifSummaryHeading.style.display = 'block'; // Showing the Motif Summary heading always
    // To handle cases with no Matches

    if (data.error) {
        sequenceOutput.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
        resultsSection.style.display = 'block';
        return;
    }

    let hasMatches = false;

    for (const [header, result] of Object.entries(data)) {
        // Display  annotated sequence
        const annotatedHeader = `<h3>${header}</h3>`;
        const annotatedSequence = `<p>${result.annotated_sequence || "No sequence available"}</p>`;
        sequenceOutput.innerHTML += `${annotatedHeader}${annotatedSequence}`;

        // Check for motif matches
        if (result.motifs.length > 0) {
            hasMatches = true;
            result.motifs.forEach((motif) => {
                const row = `
                    <tr>
                        <td>${motif.motif_id || 'N/A'}</td>
                        <td>${motif.motif_name || 'N/A'}</td>
                        <td>${motif.motif_type || 'N/A'}</td>
                        <td>${motif.start || 'N/A'}-${motif.end || 'N/A'}</td>
                        <td>${motif.sequence || 'N/A'}</td>
                        <td>${motif.description || 'N/A'}</td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        }
    }

    // Display table or "No matches found" message
    if (hasMatches) {
        summaryTable.style.display = 'table'; // Show table
    } else {
        noMatchesMessage.style.display = 'block'; // Show "No matches found" message
    }

    // Show the results section
    resultsSection.style.display = 'block';
}

