from flask import Flask, render_template, request, jsonify
from eliza import Eliza

app = Flask(__name__)

# Initialize Eliza chatbot
eliza_bot = Eliza()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['user_message']

    # Use Eliza to generate a response
    bot_response = eliza_bot.respond(user_message)

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)