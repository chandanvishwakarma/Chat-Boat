# UPSRTC Helpdesk Chatbot

A powerful and intelligent chatbot for UPSRTC (Uttar Pradesh State Road Transport Corporation) with AI-enhanced responses, comprehensive service support, and modern UI design.

## 🚀 **New Features (v2.0)**

### 🤖 **AI-Powered Responses**
- **Intelligent Context Understanding**: Advanced keyword matching and context-aware responses
- **Enhanced Response Patterns**: Multiple response variations for natural conversations
- **Smart Fallback System**: Graceful degradation when AI services are unavailable
- **Real-time Response Generation**: Dynamic response creation based on user queries

### 🎯 **Comprehensive UPSRTC Services**
- **Ticket Booking**: Complete booking assistance and guidance
- **Route Information**: Detailed route planning and information
- **Schedule Management**: Real-time bus schedules and timings
- **Fare Calculation**: Accurate fare information and pricing
- **Complaint Management**: Complaint registration and tracking
- **Contact Support**: Direct helpline and contact information
- **Mobile App Support**: App download and usage guidance
- **Website Services**: Online portal assistance

### 💬 **Enhanced User Experience**
- **Quick Action Buttons**: One-click access to common services
- **Message Timestamps**: Real-time conversation tracking
- **Professional Branding**: UPSRTC official helpdesk appearance
- **Responsive Design**: Works perfectly on all devices
- **Smooth Animations**: Professional UI interactions

### 🔧 **Technical Enhancements**
- **API Integration Ready**: Easy integration with external AI services
- **Enhanced Error Handling**: Robust error management and recovery
- **Performance Optimized**: Fast response times and efficient processing
- **Scalable Architecture**: Easy to extend and customize

## 📁 **Files Structure**

```
BA_CODE/
├── app.py                          # Enhanced Flask backend with AI integration
├── requirements.txt                # Updated Python dependencies
├── chatbot.html                   # Standalone UPSRTC helpdesk with quick actions
├── chatbot_integration.html       # Dashboard integration with enhanced features
├── index.html                     # Your existing dashboard
├── index1.html                    # Your existing dashboard
└── README.md                      # This comprehensive guide
```

## 🚀 **Quick Start**

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python app.py
```

### 3. Access the Helpdesk
- **Standalone Helpdesk**: http://localhost:5000
- **Dashboard Integration**: Open `chatbot_integration.html`

## 🎯 **How to Use**

### **Testing the Enhanced Chatbot**

1. Start the Flask server: `python app.py`
2. Open your browser: `http://localhost:5000`
3. Click the chat button (💬) in the bottom-right corner
4. Try these enhanced interactions:

#### **Quick Actions (One-Click)**
- 🎫 **Book Ticket** - Instant booking assistance
- 🗺️ **Routes** - Route information and planning
- ⏰ **Schedule** - Bus schedules and timings
- 💰 **Fare** - Fare calculation and pricing
- 📝 **Complaint** - Complaint registration
- 📞 **Contact** - Direct helpline access

#### **Natural Language Queries**
- "I want to book a ticket from Lucknow to Delhi"
- "What's the fare from Kanpur to Varanasi?"
- "Show me bus schedules for tomorrow"
- "I have a complaint about my journey"
- "How can I contact UPSRTC?"
- "Download the mobile app"
- "Visit the website"

### **Advanced Features**

#### **AI-Enhanced Responses**
The chatbot now provides:
- **Context-Aware Responses**: Understands conversation flow
- **Multiple Response Variations**: Natural, varied responses
- **Intelligent Fallbacks**: Always provides helpful information
- **Real-time Processing**: Instant response generation

#### **Service Categories**
1. **Booking Services**
   - Online booking guidance
   - Counter booking information
   - Mobile app booking
   - Payment methods

2. **Route Services**
   - Route planning
   - Destination information
   - Interstate services
   - Local route details

3. **Schedule Services**
   - Real-time schedules
   - Departure times
   - Arrival information
   - Frequency details

4. **Support Services**
   - Helpline numbers
   - Email support
   - Office locations
   - Emergency contacts

## 🔌 **API Endpoints**

### **Enhanced API Features**
- `GET /` - Main helpdesk page
- `POST /api/chat` - Enhanced chat endpoint with timestamps
- `GET /api/health` - Health check with feature list
- `GET /api/services` - Available UPSRTC services

### **Example API Usage**
```javascript
// Send a message to the enhanced chatbot
const response = await fetch('/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: 'Book a ticket from Lucknow to Delhi' })
});

const data = await response.json();
console.log(data.response); // AI-enhanced response
console.log(data.timestamp); // Response timestamp
console.log(data.source); // UPSRTC Helpdesk
```

## 🎨 **Customization Options**

### **Adding More AI Services**
You can integrate with free AI APIs:

1. **Hugging Face Inference API**
2. **OpenAI API** (with API key)
3. **Google AI** (with API key)
4. **Custom AI Models**

### **Customizing Responses**
Edit the `enhanced_responses` dictionary in `app.py`:

```python
enhanced_responses = {
    "custom_category": [
        "Your custom response 1",
        "Your custom response 2",
        "Your custom response 3"
    ]
}
```

### **Adding New Quick Actions**
Add new buttons in `chatbot.html`:

```html
<button class="quick-btn" onclick="sendQuickMessage('Your custom action')">
    🎯 Your Action
</button>
```

## 🚀 **Deployment Options**

### **Free Hosting Platforms**
1. **Heroku** - Easy deployment with Git integration
2. **Railway** - Modern platform with automatic scaling
3. **Render** - Free tier with good performance
4. **PythonAnywhere** - Python-focused hosting
5. **Vercel** - Fast deployment with serverless functions

### **Production Deployment**
For production use, consider:
- **Environment Variables** for API keys
- **Database Integration** for conversation history
- **Load Balancing** for high traffic
- **SSL Certificates** for security
- **Monitoring and Logging** for maintenance

## 🔧 **Advanced Configuration**

### **Environment Variables**
```bash
# For AI API integration
AI_API_KEY=your_api_key_here
AI_SERVICE_URL=your_service_url

# For production settings
FLASK_ENV=production
DEBUG=False
```

### **Database Integration**
Add conversation logging:
```python
# Example with SQLite
import sqlite3

def log_conversation(user_message, bot_response, timestamp):
    conn = sqlite3.connect('conversations.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO conversations (user_message, bot_response, timestamp)
        VALUES (?, ?, ?)
    ''', (user_message, bot_response, timestamp))
    conn.commit()
    conn.close()
```

## 📊 **Analytics and Monitoring**

### **Built-in Analytics**
- Message timestamps
- Response sources
- Service usage tracking
- Error monitoring

### **Custom Analytics**
Add your own tracking:
```python
def track_user_interaction(user_message, response_type):
    # Your analytics code here
    pass
```

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 **Support**

- **Technical Issues**: Check the troubleshooting section
- **Feature Requests**: Open an issue on GitHub
- **UPSRTC Services**: Use the chatbot's contact features

## 📄 **License**

This project is open source and available under the MIT License.

---

## 🎉 **What's New in v2.0**

✅ **AI-Powered Intelligence**: Smart response generation  
✅ **Quick Action Buttons**: One-click service access  
✅ **Enhanced UI/UX**: Professional helpdesk appearance  
✅ **Comprehensive Services**: Full UPSRTC service coverage  
✅ **Real-time Features**: Timestamps and live responses  
✅ **Scalable Architecture**: Easy to extend and customize  
✅ **Production Ready**: Deployment and monitoring support  

**Your UPSRTC Helpdesk is now more powerful than ever! 🚀**
