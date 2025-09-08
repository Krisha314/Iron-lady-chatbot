# Iron Lady FAQ Chatbot

A simple AI-powered chatbot that answers FAQs about **Iron Lady's leadership programs** using Python, Flask, and OpenAI GPT API.  

## Features

- Answers questions about Iron Lady programs
- Uses OpenAI GPT-3.5 for intelligent responses
- Simple web-based chat interface
- Safe API key handling using `.env`
- Easy to run locally

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (jQuery)
- **AI API:** OpenAI GPT-3.5 / GPT-4
- **Environment Management:** dotenv
- **Version Control:** Git (optional)

## Project Structure

ironlady-chatbot/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend HTML
├── .env # API key (ignored by Git)
├── requirements.txt # Python dependencies
├── .gitignore # To ignore .env and temporary files
└── README.md # Project documentation

## Setup Instructions

### 1. Clone the repository (optional)
git clone <your-repo-url>
cd ironlady-chatbot

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

4. Install dependencies

pip install -r requirements.txt

5. Add OpenAI API Key
Create a .env file in the project root:
OPENAI_API_KEY=sk-your_openai_key_here

Important: Never put your API key in the frontend. Keep it in .env.

5. Run the Flask app
python app.py
Open your browser and visit:

Local  Server 
http://127.0.0.1:5000/

Usage
Ask questions like:

What programs does Iron Lady offer?
Is the program online or offline?
Do I get a certificate?
Who are the mentors?
How long are the programs?
The chatbot will respond with answers from the FAQ context.

Security Notes
.env file is ignored in Git to prevent API key exposure.

Frontend never contains the OpenAI API key.

Revoke and regenerate API keys if accidentally exposed.
