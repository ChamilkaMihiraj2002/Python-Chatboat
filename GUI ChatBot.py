import os
import google.generativeai as genai
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(themename="darkly")  # Choose the theme, like "darkly", "superhero", etc.
app.title("AI ChatBoat with Python")
app.geometry("800x800")
app.resizable(False, False)

# Frame to hold Text widget and scrollbar
frame = ttk.Frame(app)
frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# Create the Text widget (acts like a label but supports scrolling)
text_widget = ttk.Text(frame, wrap=WORD, height=30, width=50)
text_widget.pack(side=LEFT, fill=BOTH, expand=YES)

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=text_widget.yview, bootstyle="primary")
scrollbar.pack(side=RIGHT, fill=Y)

# Add a green text tag for user input
text_widget.tag_configure("green", foreground="green")

# Configure the Text widget to work with the scrollbar
text_widget.config(yscrollcommand=scrollbar.set)

def ai():
    genai.configure(api_key="Gemini API key")

    # Create the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
      # safety_settings = Adjust safety settings
      # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    history = []

    # Get user input from the entry field
    input_text = entry_field.get()

    if input_text:  # Only proceed if the user provided some input
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(input_text)
        model_response = response.text

        # Remove any markdown-like bold formatting (*) from the response
        model_response_cleaned = model_response.replace("*", "")  # Removes the * characters

        # Print response in the text widget
        text_widget.config(state="normal")  # Enable editing temporarily to insert text
        text_widget.insert(END, f"You: {input_text}\n", "green")
        text_widget.insert(END, f"AI: {model_response_cleaned}\n\n")
        text_widget.config(state="disabled")  # Disable editing after inserting text
        text_widget.see(END)  # Scroll to the end of the text widget

        # Update chat history
        history.append({'role': 'user', 'parts': [input_text]})
        history.append({'role': 'model', 'parts': [model_response_cleaned]})

# Insert some large content into the Text widget
large_text = "HI... Today how can I help you.. \n"
text_widget.insert(END, large_text)

# Disable editing the Text widget (like a label)
text_widget.config(state=DISABLED)

# Create a Label to indicate the text entry field
label = ttk.Label(app, text="Text Here:", bootstyle="primary")
label.pack(pady=10)

# Create a text entry field (Input field)
entry_field = ttk.Entry(app, bootstyle="info", width=85,)
entry_field.pack(side=LEFT, padx=5)

# Add a button to submit or process the entry data
submit_button = ttk.Button(app, text="Sent", bootstyle="success", width=8 , command=ai)
submit_button.pack(side=LEFT, pady=10)

app.mainloop()