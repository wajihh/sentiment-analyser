from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis")
# Sample text for testing
text = "I love learning new things about AI!"

# Analyze sentiment
result = sentiment_model(text)

# Print the result
print("Sentiment:", result[0]['label'])
print("Confidence Score:", round(result[0]['score'], 2))

import streamlit as st
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

# Streamlit title and description
st.title("Sentiment Analyzer")
st.write("Enter text to determine its sentiment (positive or negative).")

# Text input box for user input
user_input = st.text_area("Enter your text here:")

# Button to analyze the sentiment
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        result = sentiment_model(user_input)
        
        # Display the sentiment and confidence score
        st.write("**Sentiment:**", result[0]['label'])
        st.write("**Confidence Score:**", round(result[0]['score'], 2))
    else:
        st.warning("Please enter some text.")

