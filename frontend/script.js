const API_BASE = "http://127.0.0.1:8000";



/* =========================================
   UPLOAD PATENT
========================================= */
async function uploadPatent() {

    const fileInput =
        document.getElementById("pdfFile");

    const status =
        document.getElementById("uploadStatus");

    const file = fileInput.files[0];

    status.innerHTML = "";

    if (!file) {

        status.innerHTML = `
            <span class="status-error">
                Please select a PDF file.
            </span>
        `;

        return;
    }

    if (file.type !== "application/pdf") {

        status.innerHTML = `
            <span class="status-error">
                Only PDF files are allowed.
            </span>
        `;

        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

        status.innerHTML = `
            <span class="status-loading">
                Uploading patent...
            </span>
        `;

        const response = await fetch(
            `${API_BASE}/upload`,
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Upload failed");
        }

        const data = await response.json();

        status.innerHTML = `
            <span class="status-success">
                ${data.message}
            </span>
        `;

    }

    catch (error) {

        console.error(error);

        status.innerHTML = `
            <span class="status-error">
                Upload failed.
            </span>
        `;
    }
}




/* =========================================
   SEARCH PATENTS
========================================= */
async function searchPatents() {

    const query =
        document.getElementById("query").value;

    const resultsDiv =
        document.getElementById("results");

    resultsDiv.innerHTML = "";

    if (!query.trim()) {

        resultsDiv.innerHTML = `
            <div class="result-card">
                <p class="status-error">
                    Please enter a patent query.
                </p>
            </div>
        `;

        return;
    }

    try {

        resultsDiv.innerHTML = `
            <div class="result-card">
                <p class="status-loading">
                    Searching similar patents...
                </p>
            </div>
        `;

        const response = await fetch(
            `${API_BASE}/similar_patents?query=${encodeURIComponent(query)}`
        );

        if (!response.ok) {
            throw new Error("Search failed");
        }

        const data = await response.json();

        console.log(data);

        resultsDiv.innerHTML = "";

        if (
            !data.results ||
            data.results.length === 0
        ) {

            resultsDiv.innerHTML = `
                <div class="result-card">
                    <p>No similar patents found.</p>
                </div>
            `;

            return;
        }


        // AI ANALYSIS CARD
        const analysisCard =
            document.createElement("div");

        analysisCard.className = "result-card";

        analysisCard.innerHTML = `
            <h2>AI Patent Analysis</h2>

            <div class="analysis-box">
                ${data.ai_analysis}
            </div>
        `;

        resultsDiv.appendChild(analysisCard);


        // RESULTS
        data.results.forEach(result => {

            const card =
                document.createElement("div");

            card.className = "result-card";

            card.innerHTML = `
                <h3>
                    ${result.patent}
                </h3>

                <div class="similarity-badge">
                    Similarity:
                    ${result.similarity_percent}%
                </div>

                <p class="result-content">
                    ${result.content}
                </p>
            `;

            resultsDiv.appendChild(card);

        });

    }

    catch (error) {

        console.error(error);

        resultsDiv.innerHTML = `
            <div class="result-card">

                <p class="status-error">
                    Error searching patents.
                </p>

            </div>
        `;
    }
}