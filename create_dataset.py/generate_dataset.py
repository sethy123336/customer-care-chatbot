import pandas as pd
import random

# Define sample queries for each intent
queries = {
    'order_tracking': [
        "Where is my order?",
        "Can you track my package?",
        "What's the status of order #12345?",
        "I haven't received my order yet",
        "Is my package delayed?",
        "When will my order arrive?",
        "Track shipment for order placed yesterday",
        "Need update on my delivery",
        "Has my order been shipped?",
        "What's the tracking number for my order?"
    ],
    'returns_info': [
        "How do I return an item?",
        "What's your return policy?",
        "Can I get a refund?",
        "Is return shipping free?",
        "How long do I have to return?",
        "I want to return a damaged product",
        "Return label request",
        "Where do I send returns?",
        "Can I exchange instead of return?",
        "Return policy for sale items"
    ],
    'faq': [
        "What are your business hours?",
        "Do you ship internationally?",
        "What payment methods do you accept?",
        "How can I change my password?",
        "Where do you ship to?",
        "Do you have a physical store?",
        "What's your phone number?",
        "How do I create an account?",
        "Are there any ongoing sales?",
        "What's your warranty policy?"
    ],
    'cancellation_request': [
        "I need to cancel my order",
        "How do I cancel a purchase?",
        "Can you stop my order from shipping?",
        "Cancel order #54321",
        "Is it too late to cancel?",
        "Want to cancel my subscription",
        "Cancel my recent purchase",
        "Need immediate order cancellation",
        "How to cancel pending order?",
        "Cancel my entire cart"
    ],
    'general_support': [
        "I need help with my account",
        "Having trouble checking out",
        "Website is not loading properly",
        "Can't add items to cart",
        "How do I contact customer service?",
        "Problem with payment processing",
        "Need assistance with order",
        "Login issues",
        "Forgot my password",
        "Technical support needed"
    ]
}

# Create lists for DataFrame
all_queries = []
all_intents = []

# Populate the lists
for intent, query_list in queries.items():
    all_queries.extend(query_list)
    all_intents.extend([intent] * len(query_list))

# Create DataFrame
df = pd.DataFrame({
    'query': all_queries,
    'intent': all_intents
})

# Shuffle the DataFrame
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv('chatbot_dataset.csv', index=False)
print("Dataset has been created successfully!")
