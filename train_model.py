import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import joblib
import os

def train_intent_classifier():
    # Load the processed dataset
    df = pd.read_csv('processed_chatbot_dataset.csv')
    
    # Split the data into features (X) and target (y)
    X = df['processed_query']
    y = df['intent']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and fit the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train the classifier
    classifier = LinearSVC(random_state=42)
    classifier.fit(X_train_tfidf, y_train)
    
    # Make predictions on test set
    y_pred = classifier.predict(X_test_tfidf)
    
    # Print classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the models
    models_dir = 'models'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
        
    joblib.dump(vectorizer, os.path.join(models_dir, 'vectorizer.joblib'))
    joblib.dump(classifier, os.path.join(models_dir, 'intent_classifier.joblib'))
    print("\nModels saved in 'models' directory")
    
    # Test with some sample queries
    sample_queries = [
        "where is my package?",
        "how do I return this item",
        "what are your store hours",
    ]
    
    print("\nTesting with sample queries:")
    # Transform the sample queries
    sample_tfidf = vectorizer.transform(sample_queries)
    # Get predictions
    sample_predictions = classifier.predict(sample_tfidf)
    
    for query, prediction in zip(sample_queries, sample_predictions):
        print(f"Query: '{query}' → Intent: {prediction}")

if __name__ == "__main__":
    print("Training intent classifier...")
    train_intent_classifier()
