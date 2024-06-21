document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('pdf-file');
    if (fileInput.files.length === 0) {
        alert('Please select a PDF file.');
        return;
    }

    const formData = new FormData();
    formData.append('pdf_file', fileInput.files[0]);

    const response = await fetch('https://your-colab-backend-url', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('extracted-text').textContent = result.text;
});
