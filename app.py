from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

@app.route("/predicao", methods=["POST"])
def predicao():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = model.generate_content(prompt)
    return jsonify({"resposta": response.text})

@app.route("/", methods=["GET"])
def home():
    return "API de Predição IA - Online"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)