from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the trained models
models_dir = 'models'
vectorizer = joblib.load(os.path.join(models_dir, 'vectorizer.joblib'))
classifier = joblib.load(os.path.join(models_dir, 'intent_classifier.joblib'))

# Define response templates for each intent
responses = {
    'order_tracking': "Your order is being processed. To track its status, please provide your order number.",
    'returns_info': "You can return items within 30 days of purchase. Please ensure the item is unused and in its original packaging.",
    'faq': "You can find detailed information in our FAQ section. Is there something specific you'd like to know?",
    'cancellation_request': "I can help you cancel your order. Please provide your order number for immediate cancellation.",
    'general_support': "I'm here to help! Could you please provide more details about your issue?"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Preprocess and predict intent
    message_tfidf = vectorizer.transform([user_message.lower()])
    predicted_intent = classifier.predict(message_tfidf)[0]
    
    # Get appropriate response
    response = responses[predicted_intent]
    
    return jsonify({
        'response': response,
        'intent': predicted_intent
    })

if __name__ == '__main__':
    app.run(debug=True)
