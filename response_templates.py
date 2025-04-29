"""
Response templates for the customer care chatbot.
Each intent has multiple possible responses and follow-up questions.
"""

responses = {
    'order_tracking': {
        'initial_responses': [
            "I'll help you track your order. Could you please provide your order number?",
            "I can check the status of your order right away. What's your order number?",
            "Let me look up your order status. Please share your order number with me."
        ],
        'no_order_number': [
            "If you don't have your order number handy, I can also look it up using your email address. Would you like to try that?",
            "No problem if you don't have the order number. We can find your order using your email address instead."
        ],
        'follow_up': [
            "Is there anything specific about your order that you'd like to know?",
            "Would you like me to send you tracking updates via email?"
        ]
    },
    'returns_info': {
        'initial_responses': [
            "I can help you with our return process. Here's what you need to know:\n• Items can be returned within 30 days of delivery\n• Items must be unused and in original packaging\n• Free return shipping for all domestic orders\nWould you like me to guide you through the return process?",
            "Our return policy is designed to make things easy for you:\n• 30-day return window\n• Free return shipping\n• Full refund to original payment method\nShall I help you start a return?",
            "Returns are hassle-free with us:\n• Start your return online\n• Print a free shipping label\n• Drop off at any carrier location\nWould you like to initiate a return now?"
        ],
        'follow_up': [
            "Do you have any specific questions about the return process?",
            "Would you like me to send you our detailed return instructions via email?"
        ]
    },
    'faq': {
        'initial_responses': [
            "I'd be happy to help you with that. Here are some key details:\n• Business hours: Mon-Fri 9AM-6PM EST\n• Customer service: 1-800-123-4567\n• Email: support@example.com\nWhat specific information are you looking for?",
            "Let me provide you with some helpful information:\n• Free shipping on orders over $50\n• International shipping available\n• Multiple payment options accepted\nIs there anything specific you'd like to know more about?"
        ],
        'follow_up': [
            "Is there anything else you'd like to know about our services?",
            "Can I help you find any other information?"
        ]
    },
    'cancellation_request': {
        'initial_responses': [
            "I'll help you with canceling your order. Please note:\n• Orders can be canceled within 1 hour of placement\n• Already shipped orders cannot be canceled\n• Refund will be processed in 3-5 business days\nCould you provide your order number for cancellation?",
            "I understand you want to cancel your order. Here's what you need to know:\n• Quick cancellation if order is not yet processed\n• Immediate confirmation of cancellation\n• Fast refund processing\nPlease share your order number to proceed."
        ],
        'follow_up': [
            "Would you like me to send you a cancellation confirmation email?",
            "Is there anything else you need assistance with regarding your cancellation?"
        ]
    },
    'general_support': {
        'initial_responses': [
            "I'm here to help! To better assist you, could you please:\n• Describe the issue you're experiencing\n• Mention any error messages you see\n• Include any relevant order numbers\nThis will help me provide the most accurate support.",
            "Thank you for reaching out. To provide you with the best possible assistance, please share:\n• What specific help you need\n• When the issue started\n• Any relevant account or order details",
            "I'll be happy to assist you. To help you more effectively, please tell me:\n• The nature of your concern\n• Any steps you've already taken\n• Your preferred resolution"
        ],
        'follow_up': [
            "Is there anything specific about this issue that you'd like me to clarify?",
            "Would you like me to connect you with a specialist for more detailed assistance?"
        ]
    }
}
