# Importing necessary libraries:
# Flask: This is a tool to help us create a web server, like a little website that our chatbot can run on.
# request: This helps us get information from the user when they send us a message.
# jsonify: This helps us send a response back to the user in a way that computers understand.
# Speller: This is a tool that helps us correct spelling mistakes in the user's message.
# pipeline: This helps us set up the chatbot using a special model that knows how to have conversations.

from flask import Flask, render_template, request, jsonify
from autocorrect import Speller
from chat import chatbot

# Create a spell checker object
spell = Speller()

#We create a new web app called app. This app will handle the messages that the user sends and the responses our chatbot gives
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = str(request.form['messageText'])

    # Handle the grammar correction
    corrected_text = spell(message)
    print(corrected_text)

    bot_response = chatbot(corrected_text)
    # print(bot_response)

    # Sending response back to user
    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
