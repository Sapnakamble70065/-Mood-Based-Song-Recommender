# app.py

import streamlit as st
from textblob import TextBlob

# Predefined song list based on mood
song_db = {
    "happy": [
        "🎵 Happy – Pharrell Williams",
        "🎵 Uptown Funk – Bruno Mars",
        "🎵 Good Life – OneRepublic"
    ],
    "sad": [
        "🎵 Someone Like You – Adele",
        "🎵 Fix You – Coldplay",
        "🎵 Let Her Go – Passenger"
    ],
    "neutral": [
        "🎵 Let It Be – The Beatles",
        "🎵 Counting Stars – OneRepublic",
        "🎵 Sunflower – Post Malone"
    ]
}

st.set_page_config(page_title="Mood-based Song Recommender")

st.title("🎶 Mood-based Song Recommender")
st.write("Type a sentence about how you're feeling and get 3 song suggestions based on your mood!")

user_input = st.text_area("📝 Enter your mood description here:")

if st.button("Recommend Songs"):
    if user_input.strip() == "":
        st.warning("Please enter something!")
    else:
        # Sentiment analysis
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0.3:
            mood = "happy"
        elif polarity < -0.3:
            mood = "sad"
        else:
            mood = "neutral"

        st.success(f"Detected Mood: **{mood.capitalize()}**")
        st.markdown("### 🎧 Your Song Recommendations:")
        for song in song_db[mood]:
            st.markdown(f"- {song}")
