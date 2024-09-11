from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import PyPDF2
from transformers import pipeline
from flask import Flask
from flask_cors import CORS
import re


import contractions
# app = Flask(__name__)


app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# model = AutoModelForSeq2SeqLM.from_pretrained("google/longt5-tglobal-base")
# tokenizer = AutoTokenizer.from_pretrained("google/longt5-tglobal-base")
summarizer = pipeline("summarization", model="google/long-t5-tglobal-base")
# summarizer = pipeline("summarization",model=tokenizer)
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def preprocess_text(text):
  # 1. Handle contractions
  text = contractions.fix(text)

  # 2. Remove numbers
  text = re.sub(r'\d+', '', text)

  # 3. Dealing with Accents and Diacritics
  # (This is a simplified example, you might need more sophisticated methods)
  text = text.encode('ascii', 'ignore').decode('ascii')

  # 4. Lowercasing
  text = text.lower()

  # 5. Remove punctuations
  text = re.sub(r'[^\w\s]', '', text)

  # 6. Tokenization (Basic split by whitespace)
  tokens = text.split()

  # 7. Remove common stop words (This is a simplified list)
  stop_words = ["a", "an", "the", "is", "are", "was", "were", "in", "on", "at", "to", "for", "of", "and", "or", "but", "not", "with", "as", "by", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]
  tokens = [word for word in tokens if word not in stop_words]

  # 8. Stemming (This is a very basic stemming approach)
  # ... (You would need to implement a more robust stemming algorithm)

  # 9. Lemmatization (This requires a more advanced library)
  # ... (You would need to integrate a lemmatization library)

  # 10. Spell checking (This is a basic example, consider using more advanced spell checkers)
  # ... (You would need to integrate a spell checker library here)

  # Join the tokens back into a string
  processed_text = ' '.join(tokens)

  return processed_text




@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        processed_text = preprocess_text(text)

        summary = summarizer(processed_text, max_length=1024, min_length=30, do_sample=False)[0]['summary_text']
        
        return jsonify({"summary": summary})

    return jsonify({"error": "Invalid file format"}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, host="0.0.0.0", port=5000)
