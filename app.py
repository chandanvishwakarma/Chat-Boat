from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import random
import os

app = Flask(__name__)
CORS(app)

# Simple chatbot responses
chatbot_responses = {
    "hello": ["Hello! How can I help you today?", "Hi there! Welcome to our website!", "Hello! Nice to meet you!"],
    "help": ["I can help you with general questions about our services.", "What would you like to know?", "I'm here to assist you!"],
    "services": ["We offer various services including data analysis, reporting, and dashboard solutions.", "Our services include business analytics and performance tracking."],
    "contact": ["You can contact us through email or phone. Would you like our contact details?", "For support, please reach out to our team."],
    "dashboard": ["Our dashboard provides real-time analytics and performance metrics.", "The dashboard shows BA performance data across different states."],
    "default": ["I'm not sure I understand. Could you please rephrase that?", "I'm still learning. Can you ask something else?", "I don't have information about that yet."]
}

def get_bot_response(user_message):
    user_message = user_message.lower().strip()
    if any(word in user_message for word in ["hello", "hi", "hey"]):
        return random.choice(chatbot_responses["hello"])
    elif any(word in user_message for word in ["help", "assist", "support"]):
        return random.choice(chatbot_responses["help"])
    elif any(word in user_message for word in ["service", "offer", "provide"]):
        return random.choice(chatbot_responses["services"])
    elif any(word in user_message for word in ["contact", "email", "phone", "reach"]):
        return random.choice(chatbot_responses["contact"])
    elif any(word in user_message for word in ["dashboard", "analytics", "performance"]):
        return random.choice(chatbot_responses["dashboard"])
    else:
        return random.choice(chatbot_responses["default"])

@app.route('/')
def home():
    # Serve chatbot.html from the current directory
    return send_file(os.path.join(os.path.dirname(__file__), 'chatbot.html'))

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        bot_response = get_bot_response(user_message)
        return jsonify({
            'response': bot_response,
            'user_message': user_message
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Chatbot is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
