import streamlit as st
from feedback_classifier import get_sentiment
from suggestion_engine import generate_suggestion

st.set_page_config(page_title="MessMate 🍽️", layout="centered")
st.title("MessMate – Smart Mess Feedback Analyzer")

feedback = st.text_area("Enter your feedback:")

if st.button("Analyze"):
    if feedback.strip() == "":
        st.warning("Please enter some feedback first!")
    else:
        sentiment = get_sentiment(feedback)
        suggestion = generate_suggestion(feedback)
        
        st.success(f"Sentiment: {sentiment.capitalize()}")
        st.info(f"Suggestion: {suggestion}")
