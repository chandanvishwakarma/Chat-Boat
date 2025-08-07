# URTC Website Chatbot

A simple and modern chatbot implementation for your URTC website using Python Flask backend and a beautiful floating chat widget.

## Features

- 🤖 **Simple AI Responses**: Basic keyword-based responses for common queries
- 💬 **Floating Chat Widget**: Modern, responsive chat interface that doesn't interfere with your website
- 🎨 **Beautiful UI**: Clean, professional design with smooth animations
- 📱 **Mobile Responsive**: Works perfectly on all device sizes
- ⚡ **Real-time**: Instant responses with typing indicators
- 🔧 **Easy Integration**: Simple to add to any existing website

## Files Structure

```
BA_CODE/
├── app.py                          # Flask backend server
├── requirements.txt                # Python dependencies
├── templates/
│   └── chatbot.html               # Standalone chatbot page
├── chatbot_integration.html       # Example with existing dashboard
├── index.html                     # Your existing dashboard
├── index1.html                    # Your existing dashboard
└── README.md                      # This file
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python app.py
```

### 3. Access the Chatbot

- **Standalone Chatbot**: http://localhost:5000
- **Dashboard with Chatbot**: Open `chatbot_integration.html` in your browser

## How to Use

### Testing the Chatbot

1. Start the Flask server using `python app.py`
2. Open your browser and go to `http://localhost:5000`
3. Click the chat button in the bottom-right corner
4. Try these example messages:
   - "Hello"
   - "What services do you offer?"
   - "How can I contact you?"
   - "Tell me about the dashboard"
   - "I need help"

### Integrating with Your Existing Website

The chatbot can be easily integrated into your existing website. Here's how:

1. **Copy the CSS styles** from the `<style>` section in `chatbot_integration.html`
2. **Copy the HTML widget** (the `<div class="chat-widget">` section)
3. **Copy the JavaScript functions** (all the chat-related functions)
4. **Add them to your existing HTML file**

### Customizing Responses

Edit the `chatbot_responses` dictionary in `app.py` to customize the bot's responses:

```python
chatbot_responses = {
    "hello": ["Hello! How can I help you today?", "Hi there! Welcome!"],
    "services": ["We offer data analysis, reporting, and dashboard solutions."],
    "contact": ["You can contact us through email or phone."],
    # Add more categories and responses
}
```

## API Endpoints

- `GET /` - Main chatbot page
- `POST /api/chat` - Chat endpoint (expects JSON with `message` field)
- `GET /api/health` - Health check endpoint

### Example API Usage

```javascript
// Send a message to the chatbot
const response = await fetch('/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: 'Hello' })
});

const data = await response.json();
console.log(data.response); // Bot's response
```

## Customization Options

### Changing Colors

Modify the CSS variables in the style section:

```css
.chat-toggle {
    background-color: #3b82f6; /* Change this to your brand color */
}

.chat-header {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8); /* Change gradient */
}
```

### Changing Position

Modify the `.chat-widget` CSS:

```css
.chat-widget {
    position: fixed;
    bottom: 20px;    /* Distance from bottom */
    right: 20px;     /* Distance from right */
    z-index: 1000;   /* Layer order */
}
```

### Adding More Responses

Extend the `get_bot_response` function in `app.py`:

```python
def get_bot_response(user_message):
    user_message = user_message.lower().strip()
    
    # Add more keyword checks
    if any(word in user_message for word in ["pricing", "cost", "price"]):
        return "Our pricing varies based on your requirements. Please contact us for a quote."
    elif any(word in user_message for word in ["schedule", "meeting", "appointment"]):
        return "I can help you schedule a meeting. What time works best for you?"
    # ... existing code
```

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
   ```

2. **CORS errors**: The Flask-CORS extension is already included, but if you're still having issues, check your browser's developer console.

3. **Chatbot not responding**: Make sure the Flask server is running and accessible at the correct URL.

### Debug Mode

The Flask app runs in debug mode by default. You'll see detailed error messages in the console if something goes wrong.

## Next Steps

To enhance this chatbot, you could:

1. **Add a Database**: Store conversation history and user preferences
2. **Integrate with AI Services**: Connect to OpenAI, Google AI, or other AI services
3. **Add Authentication**: Require users to log in before chatting
4. **File Upload**: Allow users to upload files and get responses
5. **Multi-language Support**: Add support for multiple languages
6. **Analytics**: Track chat usage and popular questions

## Support

If you encounter any issues or have questions about customizing the chatbot, feel free to ask!

## License

This project is open source and available under the MIT License.
