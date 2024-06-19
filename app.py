nano app.py

from flask import Flask, request, render_template_string
import pytesseract
from pdf2image import convert_from_path
import markdown
import os

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>PDF to Text</title>
</head>
<body>
    <h1>PDF to Text Converter</h1>
    <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="pdf_file">
        <input type="submit" value="Convert">
    </form>
    {% if text %}
    <h2>Extracted Text</h2>
    <pre>{{ text }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    text = None
    if request.method == 'POST':
        file = request.files['pdf_file']
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            # PDFファイルを画像に変換
            images = convert_from_path(file_path)

            # Tesseractで画像からテキストを抽出
            text = ""
            for image in images:
                text += pytesseract.image_to_string(image, lang='jpn_vert')

            # Markdown形式に変換
            text = markdown.markdown(text)
    return render_template_string(HTML_TEMPLATE, text=text)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
