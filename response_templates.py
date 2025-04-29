"""Response templates for the customer care chatbot.
Focused on providing clear, consistent responses for common customer service scenarios.
"""

responses = {
    'order_tracking': {
        'initial_responses': [
            "📦 To track your order, I'll need your order number. Once you provide it, I can tell you:\n• Current order status\n• Estimated delivery date\n• Shipping carrier information\n\nPlease share your order number."
        ],
        'no_order_number': [
            "No order number? No problem! I can look up your order using your email address. Please provide the email address used for the order."
        ],
        'follow_up': [
            "Would you like to:\n• Get detailed tracking information\n• Set up delivery notifications\n• See the order contents\n\nJust let me know what you need."
        ]
    },
    'returns_info': {
        'initial_responses': [
            "📋 Here's our return policy:\n• 30-day return window from delivery date\n• Free return shipping on all orders\n• Full refund to original payment method\n• Items must be unused with original packaging\n\nWould you like to start a return?"
        ],
        'follow_up': [
            "To process your return, I can help you:\n• Generate a return shipping label\n• Track your refund status\n• Find the nearest drop-off location\n\nWhat would you like to do?"
        ]
    },
    'faq': {
        'initial_responses': [
            "ℹ️ Here are our key business details:\n• Hours: Monday-Friday, 9AM-6PM EST\n• Phone: 1-800-123-4567\n• Email: support@example.com\n• Free shipping on orders over $50\n• International shipping available\n\nWhat else would you like to know?"
        ],
        'follow_up': [
            "I can provide more information about:\n• Shipping options and rates\n• Payment methods\n• Account management\n• Current promotions\n\nWhich topic interests you?"
        ]
    },
    'cancellation_request': {
        'initial_responses': [
            "❌ Order Cancellation Information:\n• Orders can be cancelled within 1 hour of placement\n• Immediate cancellation confirmation\n• Refund processed in 3-5 business days\n\nTo cancel your order, please provide your order number."
        ],
        'follow_up': [
            "Once you provide the order number, I can:\n• Process the cancellation\n• Send a confirmation email\n• Initiate your refund\n\nPlease share your order number to proceed."
        ]
    },
    'general_support': {
        'initial_responses': [
            "🛠️ I'm here to help! To assist you better, please provide:\n• A brief description of your issue\n• Any error messages you're seeing\n• Your order number (if applicable)\n\nThis will help me provide the most relevant solution."
        ],
        'follow_up': [
            "Based on your issue, I can:\n• Troubleshoot technical problems\n• Connect you with a specialist\n• Provide step-by-step guidance\n\nHow would you like to proceed?"
        ]
    }
}
