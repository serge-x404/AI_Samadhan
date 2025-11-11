from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  

app = Flask(__name__)
CORS(app, origins=["http://localhost:5500"])

# API_KEY = "GOOGLE.COM API"
#API_URL = "https://api.openai.com/v1/images/generations"

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt', '')

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "n": 1,
        "size": "512x512"
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        return jsonify({"image_url": image_url})
    else:
        return jsonify({"error": "Failed to generate image"}), 500

if __name__ == "__main__":
    app.run(debug=True)