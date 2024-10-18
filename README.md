# AI ChatBot with Python

This project is a desktop AI ChatBot built using Python, `ttkbootstrap` for the GUI, and Google’s Generative AI API for AI-based conversations. The app provides an interactive chatbot experience where users can ask questions, and the AI model generates responses based on the input.

## Features
- **AI Chat Integration**: Connects with Google’s Generative AI API (`gemini-1.5-flash`) to process user queries and respond.
- **GUI with `ttkbootstrap`**: A clean, modern desktop application interface using `ttkbootstrap`, featuring themes like "darkly" and others.
- **Text Scrolling Support**: The text display area supports large messages with scrolling and the ability to handle dynamic responses.
- **User Input Validation**: Ensures that empty inputs are not processed.
- **Response Formatting**: User input and AI responses are styled with distinct colors to enhance readability.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ChamilkaMihiraj2002/Python-Chatboat.git
   cd ai-chatbot-python
Create a Python virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Create an account with Google Generative AI and obtain an API key.

Configure the API key:

Replace the api_key in the ai() function with your generated API key from Google Generative AI.
Run the app:

bash
Copy code
python app.py

Usage
Type your question or prompt into the entry field at the bottom.
Press the Sent button to send your input to the AI model.
The AI's response will appear in the text area with scrolling support.
Dependencies
ttkbootstrap: For creating the user interface with various themes.
google-generativeai: For accessing Google's Gemini 1.5 model and generating AI responses.
os: Used for basic file handling and environment setup.
You can install the dependencies using:


pip install ttkbootstrap google-generativeai









