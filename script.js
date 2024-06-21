document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('pdf-file');
    if (fileInput.files.length === 0) {
        alert('Please select a PDF file.');
        return;
    }

    const formData = new FormData();
    formData.append('pdf_file', fileInput.files[0]);

    try {
        const response = await fetch('https://54ac-104-154-218-253.ngrok-free.app/', {  // ここにngrokのパブリックURLを設定
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        document.getElementById('extracted-text').textContent = result.text;
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
});
