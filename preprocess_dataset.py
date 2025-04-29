import pandas as pd
import spacy
import os

def preprocess_text(text, nlp):
    # Convert to lowercase
    text = text.lower()
    
    # Create spaCy doc
    doc = nlp(text)
    
    # Tokenize and remove punctuation and whitespace
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    
    # Join tokens back together with spaces
    return ' '.join(tokens)

def main():
    # Load spaCy model
    try:
        nlp = spacy.load('en_core_web_sm')
    except OSError:
        print("Downloading spaCy model...")
        os.system('python -m spacy download en_core_web_sm')
        nlp = spacy.load('en_core_web_sm')

    # Read the dataset
    input_file = 'create_dataset.py/chatbot_dataset.csv'
    df = pd.read_csv(input_file)
    
    # Preprocess the queries
    print("Preprocessing queries...")
    df['processed_query'] = df['query'].apply(lambda x: preprocess_text(x, nlp))
    
    # Save the processed dataset
    output_file = 'processed_chatbot_dataset.csv'
    df.to_csv(output_file, index=False)
    print(f"Processed dataset saved to {output_file}")
    
    # Display sample of processed queries
    print("\nSample of processed queries:")
    print(df[['query', 'processed_query']].head())

if __name__ == "__main__":
    main()
