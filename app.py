from flask import Flask, jsonify, request, render_template, send_from_directory
import os
import json
from model import get_result, doc_to_img_dir  # Import the necessary functions
from search import search_text_in_json
app = Flask(__name__)




# Load the merged JSON file once when the server starts
with open('D:/VSCODE/Ai_model/merged_videos.json', 'r', encoding='utf-8') as f:
    video_data = json.load(f)["videos"]

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = get_result(query)  # You can use a different function if needed
    img_paths = doc_to_img_dir(results)
    result = {'paths': img_paths}
    print("Search query (search):", query)
    print("Image paths (search):", img_paths)
    return jsonify(result)

@app.route('/search_ocr')
def search_ocr():
    query = request.args.get('query', '').lower()
    img_paths = search_text_in_json(query)
    result = {'paths': img_paths}
    print("Search query:", query)
    print("Image paths:", img_paths)
    return jsonify(result)

@app.route('/images/<path:filename>')
def serve_images(filename):
    full_path = os.path.join('D:/MyDrive/Real_data', filename)
    print("Full path being served:", full_path)
    if os.path.exists(full_path):
        return send_from_directory('D:/MyDrive/Real_data', filename)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
