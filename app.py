from flask import Flask, render_template, request, jsonify
import joblib
import os
import random
from response_templates import responses

app = Flask(__name__)

# Load the trained models
models_dir = 'models'
vectorizer = joblib.load(os.path.join(models_dir, 'vectorizer.joblib'))
classifier = joblib.load(os.path.join(models_dir, 'intent_classifier.joblib'))

# Store conversation history
conversations = {}

@app.route('/')
def home():
    return render_template('index.html')

def get_response(intent, session_id):
    # Get conversation state for this session
    conversation = conversations.get(session_id, {
        'message_count': 0,
        'last_intent': None,
        'follow_up_sent': False
    })
    
    # Update conversation state
    conversation['message_count'] += 1
    conversation['last_intent'] = intent
    
    # Select appropriate response
    intent_responses = responses[intent]
    
    if conversation['message_count'] == 1 or not conversation['follow_up_sent']:
        # Send initial response
        response = random.choice(intent_responses['initial_responses'])
        
        # For certain intents, add no_order_number response if available
        if intent in ['order_tracking', 'cancellation_request'] and 'no_order_number' in intent_responses:
            if random.random() < 0.3:  # 30% chance to add this info
                response += "\n\n" + random.choice(intent_responses['no_order_number'])
        
        conversation['follow_up_sent'] = False
    else:
        # Send follow-up if available, otherwise send initial response
        if 'follow_up' in intent_responses and not conversation['follow_up_sent']:
            response = random.choice(intent_responses['follow_up'])
            conversation['follow_up_sent'] = True
        else:
            response = random.choice(intent_responses['initial_responses'])
            conversation['follow_up_sent'] = False
    
    # Update conversation store
    conversations[session_id] = conversation
    
    return response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    session_id = request.headers.get('X-Session-ID', 'default')
    
    # Preprocess and predict intent
    message_tfidf = vectorizer.transform([user_message.lower()])
    predicted_intent = classifier.predict(message_tfidf)[0]
    
    # Get appropriate response
    response = get_response(predicted_intent, session_id)
    
    return jsonify({
        'response': response,
        'intent': predicted_intent
    })

if __name__ == '__main__':
    app.run(debug=True)
