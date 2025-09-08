from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

FAQ_CONTEXT = """
You are a helpful assistant for Iron Lady's leadership programs. Only answer based on these facts:
Programs: Women in Leadership, Returnship Programs, Executive Presence Masterclass, Leadership for Entrepreneurs
Duration: 4–12 weeks
Mode: Online
Certificates: Yes
Mentors: Industry experts, corporate leaders, certified leadership coaches
"""

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": FAQ_CONTEXT},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    answer = ask_openai(user_input)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
