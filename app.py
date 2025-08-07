from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import random
import os
import requests
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Enhanced chatbot responses with more categories
chatbot_responses = {
    "greeting": [
        "Hello! Welcome to UPSRTC Helpdesk. How can I assist you today?",
        "Hi there! I'm your UPSRTC assistant. What can I help you with?",
        "Welcome to UPSRTC! I'm here to help you with any questions or support you need.",
        "Greetings! How may I assist you with UPSRTC services today?"
    ],
    "help": [
        "I can help you with various UPSRTC services including ticket booking, route information, schedules, complaints, and general support. What specific assistance do you need?",
        "I'm here to help with UPSRTC services. I can assist with bookings, routes, schedules, and more. What would you like to know?",
        "I can provide information about UPSRTC services, help with bookings, routes, and answer your questions. How can I help?"
    ],
    "booking": [
        "For ticket booking, you can visit our official website or use our mobile app. You can also book tickets at any UPSRTC counter. Would you like route information?",
        "To book tickets, visit upsrtc.up.gov.in or use our mobile app. You can also call our helpline or visit any UPSRTC counter.",
        "Ticket booking is available online at our website, through our mobile app, or at any UPSRTC counter. What route are you looking for?"
    ],
    "routes": [
        "UPSRTC operates buses across Uttar Pradesh and to major cities in India. I can help you find specific routes. Which route are you interested in?",
        "We have extensive route coverage across UP and major Indian cities. Please specify your source and destination for detailed information.",
        "UPSRTC connects all major cities in Uttar Pradesh and provides interstate services. Where do you want to travel from and to?"
    ],
    "schedule": [
        "Bus schedules vary by route and time. Please specify your route and preferred time for accurate schedule information.",
        "I can help you find bus schedules. Please tell me your source, destination, and preferred travel time.",
        "Schedules are available for all routes. Please provide your travel details for specific timing information."
    ],
    "complaint": [
        "For complaints, you can call our helpline, email us, or use our online complaint portal. Please provide details of your issue.",
        "We take complaints seriously. You can register complaints through our helpline, email, or online portal. What's your concern?",
        "To file a complaint, contact our helpline or use our online complaint system. Please describe your issue."
    ],
    "contact": [
        "You can contact UPSRTC through our helpline: 1800-180-8287, email: info@upsrtc.up.gov.in, or visit any UPSRTC office.",
        "For support, call our helpline 1800-180-8287, email us at info@upsrtc.up.gov.in, or visit our website.",
        "Contact us at helpline: 1800-180-8287, email: info@upsrtc.up.gov.in, or visit any UPSRTC counter."
    ],
    "fare": [
        "Fares vary based on distance, bus type, and route. Please specify your source and destination for accurate fare information.",
        "I can help you find fare information. Please provide your travel details including source, destination, and preferred bus type.",
        "Fare calculation depends on distance and bus type. Please share your travel route for specific fare details."
    ],
    "bus_types": [
        "UPSRTC offers various bus types: Ordinary, Express, AC, Volvo, and Luxury buses. Which type are you interested in?",
        "We have Ordinary, Express, AC, Volvo, and Luxury buses. Each has different amenities and pricing. What's your preference?",
        "Available bus types include Ordinary, Express, AC, Volvo, and Luxury. Each offers different comfort levels and pricing."
    ],
    "refund": [
        "Refund policies vary by ticket type. For online bookings, refunds are processed through the same payment method. Please contact our helpline for assistance.",
        "Refunds are available as per our policy. Online ticket refunds are processed automatically. For counter tickets, visit any UPSRTC office.",
        "For refunds, online tickets are refunded automatically. Counter tickets require visiting UPSRTC office. Please contact our helpline for details."
    ],
    "emergency": [
        "For emergencies, please call our 24/7 helpline: 1800-180-8287 or contact the nearest UPSRTC office immediately.",
        "In case of emergency, call our helpline 1800-180-8287 or contact the nearest UPSRTC office for immediate assistance.",
        "Emergency support is available 24/7. Call 1800-180-8287 or visit the nearest UPSRTC office for immediate help."
    ],
    "website": [
        "Visit our official website: upsrtc.up.gov.in for complete information, online booking, and services.",
        "Our website upsrtc.up.gov.in provides comprehensive information, online booking, and all UPSRTC services.",
        "For detailed information and online services, visit upsrtc.up.gov.in"
    ],
    "mobile_app": [
        "Download our mobile app 'UPSRTC' from Google Play Store or Apple App Store for easy booking and services.",
        "Our mobile app 'UPSRTC' is available on Google Play Store and Apple App Store for convenient booking.",
        "Get our mobile app 'UPSRTC' from app stores for easy access to booking and services."
    ],
    "default": [
        "I'm here to help with UPSRTC services. Could you please be more specific about what you need assistance with?",
        "I can help with bookings, routes, schedules, complaints, and general UPSRTC information. What would you like to know?",
        "I'm your UPSRTC assistant. I can help with various services. Please let me know what specific information you need.",
        "I'm here to assist you with UPSRTC services. Could you please clarify your question so I can provide better help?"
    ]
}

# Enhanced keyword patterns for better matching
keyword_patterns = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "namaste", "namaskar"],
    "help": ["help", "assist", "support", "guide", "what can you do", "how can you help"],
    "booking": ["book", "booking", "ticket", "reserve", "buy ticket", "purchase", "online booking"],
    "routes": ["route", "destination", "source", "from", "to", "travel", "journey", "path"],
    "schedule": ["schedule", "time", "timing", "departure", "arrival", "when", "bus time"],
    "complaint": ["complaint", "problem", "issue", "grievance", "feedback", "report", "wrong", "bad"],
    "contact": ["contact", "phone", "call", "email", "helpline", "number", "reach", "connect"],
    "fare": ["fare", "price", "cost", "amount", "money", "payment", "charge", "rate"],
    "bus_types": ["bus type", "ordinary", "express", "ac", "volvo", "luxury", "comfort", "amenities"],
    "refund": ["refund", "cancel", "cancellation", "return", "money back", "reimbursement"],
    "emergency": ["emergency", "urgent", "immediate", "critical", "accident", "breakdown"],
    "website": ["website", "web", "online", "internet", "site", "portal"],
    "mobile_app": ["app", "mobile", "android", "iphone", "download", "application"]
}

def get_ai_response(user_message):
    """Get response from free AI API (using a simple approach)"""
    try:
        # Using a simple AI service for enhanced responses
        # You can replace this with any free AI API
        api_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
        
        # For now, we'll use a simple pattern matching with AI-like responses
        # In production, you can integrate with OpenAI, Hugging Face, or other free APIs
        
        # Enhanced response patterns
        enhanced_responses = {
            "greeting": [
                "Namaste! Welcome to UPSRTC Helpdesk. I'm here to assist you with all your travel needs. How may I help you today?",
                "Hello! I'm your UPSRTC virtual assistant. I can help you with bookings, routes, schedules, and more. What would you like to know?",
                "Welcome to UPSRTC! I'm ready to help you with ticket booking, route information, and any other services you need."
            ],
            "booking": [
                "I can help you book tickets! You can book online at upsrtc.up.gov.in, use our mobile app, or visit any UPSRTC counter. Which method would you prefer?",
                "For ticket booking, you have multiple options: our website, mobile app, or counter booking. What's your preferred source and destination?",
                "Let me help you with ticket booking. Please tell me your source, destination, and preferred travel date."
            ],
            "route": [
                "I can help you find the best route! UPSRTC operates across Uttar Pradesh and major Indian cities. Where do you want to travel from and to?",
                "Route information is available for all UPSRTC services. Please specify your source and destination for detailed route options.",
                "I'll help you find the perfect route. Please tell me your starting point and destination."
            ],
            "schedule": [
                "I can provide you with bus schedules. Please tell me your route and preferred travel time for accurate timing information.",
                "Let me check the schedule for you. Please specify your source, destination, and preferred departure time.",
                "I'll find the best schedule for your journey. Please provide your travel details."
            ],
            "fare": [
                "I can help you with fare information. Fares depend on distance, bus type, and route. Please specify your travel details.",
                "Let me calculate the fare for you. Please tell me your source, destination, and preferred bus type.",
                "I'll provide you with accurate fare information. Please share your travel route and bus preference."
            ],
            "complaint": [
                "I'm sorry to hear you have a complaint. I can help you file it through our helpline, email, or online portal. Please describe your issue.",
                "We take complaints seriously. I can guide you through the complaint process. Please provide details of your concern.",
                "I'll help you register your complaint. You can call our helpline or use our online system. What's the issue?"
            ]
        }
        
        # Simple AI-like response selection based on context
        user_lower = user_message.lower()
        
        if any(word in user_lower for word in ["book", "ticket", "reserve"]):
            return random.choice(enhanced_responses["booking"])
        elif any(word in user_lower for word in ["route", "from", "to", "destination"]):
            return random.choice(enhanced_responses["route"])
        elif any(word in user_lower for word in ["schedule", "time", "when", "departure"]):
            return random.choice(enhanced_responses["schedule"])
        elif any(word in user_lower for word in ["fare", "price", "cost", "amount"]):
            return random.choice(enhanced_responses["fare"])
        elif any(word in user_lower for word in ["complaint", "problem", "issue", "bad"]):
            return random.choice(enhanced_responses["complaint"])
        elif any(word in user_lower for word in ["hello", "hi", "hey", "namaste"]):
            return random.choice(enhanced_responses["greeting"])
        
        # If no specific pattern matches, return None to use the regular response system
        return None
        
    except Exception as e:
        print(f"AI Response Error: {e}")
        return None

def get_bot_response(user_message):
    """Get an intelligent response from the chatbot"""
    user_message = user_message.lower().strip()
    
    # Try AI response first
    ai_response = get_ai_response(user_message)
    if ai_response and len(ai_response) > 10:
        return ai_response
    
    # Enhanced keyword matching with context
    matched_category = None
    max_matches = 0
    
    for category, keywords in keyword_patterns.items():
        matches = sum(1 for keyword in keywords if keyword in user_message)
        if matches > max_matches:
            max_matches = matches
            matched_category = category
    
    # Special handling for specific queries
    if any(word in user_message for word in ["upsrtc", "bus", "transport"]):
        if "website" in user_message or "online" in user_message:
            return random.choice(chatbot_responses["website"])
        elif "app" in user_message or "mobile" in user_message:
            return random.choice(chatbot_responses["mobile_app"])
        elif "contact" in user_message or "call" in user_message:
            return random.choice(chatbot_responses["contact"])
    
    # Handle route queries
    if any(word in user_message for word in ["from", "to", "route", "destination"]):
        return random.choice(chatbot_responses["routes"])
    
    # Handle booking queries
    if any(word in user_message for word in ["book", "ticket", "reserve"]):
        return random.choice(chatbot_responses["booking"])
    
    # Handle fare queries
    if any(word in user_message for word in ["fare", "price", "cost", "amount"]):
        return random.choice(chatbot_responses["fare"])
    
    # Handle complaint queries
    if any(word in user_message for word in ["complaint", "problem", "issue", "bad"]):
        return random.choice(chatbot_responses["complaint"])
    
    # Handle emergency queries
    if any(word in user_message for word in ["emergency", "urgent", "accident"]):
        return random.choice(chatbot_responses["emergency"])
    
    # Return matched category response or default
    if matched_category and matched_category in chatbot_responses:
        return random.choice(chatbot_responses[matched_category])
    
    return random.choice(chatbot_responses["default"])

@app.route('/')
def home():
    return send_file(os.path.join(os.path.dirname(__file__), 'chatbot.html'))

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get intelligent response
        bot_response = get_bot_response(user_message)
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return jsonify({
            'response': bot_response,
            'user_message': user_message,
            'timestamp': timestamp,
            'source': 'UPSRTC Helpdesk'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy', 
        'message': 'UPSRTC Helpdesk is running',
        'version': '2.0',
        'features': ['AI-powered responses', 'Enhanced keyword matching', 'UPSRTC services support']
    })

@app.route('/api/services')
def services():
    """API endpoint to get available UPSRTC services"""
    services = {
        'booking': 'Ticket booking services',
        'routes': 'Route information and planning',
        'schedules': 'Bus schedules and timings',
        'complaints': 'Complaint registration and tracking',
        'refunds': 'Ticket cancellation and refunds',
        'contact': 'Customer support and helpline',
        'mobile_app': 'Mobile application services',
        'website': 'Online portal services'
    }
    return jsonify(services)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
