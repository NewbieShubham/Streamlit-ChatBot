import streamlit as st
from transformers import pipeline

conversational_model = pipeline("text-generation", model="microsoft/DialoGPT-large")
# Predefined responses mapping
response_map = {
    "Hi": "Hello! how are you doing?😁",
    "hi": "Hello! how are you doing?😁",
    "Hii": "Hello! how are you doing?😁",
    "hii": "Hello! how are you doing?😁",
    "Hiii": "Hello! What you doing?😁",
    "hiii": "Hello! What you doing?😁",
    "fine": "Good to hear this, so what's on your mind?",
    "Fine": "Good to hear this, so what's on your mind?",
    "great": "Good to hear this, so what's on your mind?",
    "Great": "Good to hear this, so what's on your mind?",
    "Fine what about you?": "I'm doing great too.",
    "I feel a bit down today": "I’m here for you. Want to talk about it?",
    "What’s your favorite thing to do when you’re feeling low?": "I believe in the importance of having deep talks!",
    "I had a rough day": "I’m sorry to hear that. What happened?",
    "I feel so lonely": "You’re not alone—I’m always here for you, anytime you need.",
    "No one seems to care about me": "That sounds really tough, but I care about you, and I’m always here if you need.",
    "I just want someone to talk to": "I’m always here for you. Let’s talk about anything you like",
    "I don’t know what to do anymore": "It’s okay to feel lost sometimes. I’m here to help you through it.",
    "I feel like no one understands me": "That must be really hard. I’m here to try to understand and support you.",
    "I just want to feel better": "I’m with you! Let’s find something to cheer you up. How about your favorite music?",
    "Thanks, I feel better talking to you": "I’m really glad to hear that! Anytime you need me, I’m here.",
    "What are you up to today?": "Not much, just hanging out with my favorite person—You!",
    "Thanks, it helps just talking to you": "I’m really glad hear that,You can talk to me whenever you feel like this",
    "Thanks for being here": "Of course! You can always count on me. :)"
}

conversation_history = []

# Streamlit interface
st.title("Newbie - A Friendly Chatbot")
st.write("Welcome to Newbie! Let's have a chat 😊")

name = st.text_input("May I know your name?", placeholder="Enter your name")
if name:
    st.write(f"Hii {name}, Hope you're doing well! Wanna have a talk?")

# Text area for user input
user_input = st.text_input("You:", placeholder="Type your message here")

# Function to generate chatbot response
if user_input:
    if user_input.lower() == 'bye':
        st.write("Newbie: Have a good day!")
    else:
        if user_input in response_map:
            bot_response = response_map[user_input]
        else:
            conversation_history.append(user_input)
            # Generate a response
            generated_responses = conversational_model(" ".join(conversation_history), max_length=100,
                                                       num_return_sequences=1)
            bot_response = generated_responses[0]['generated_text']

            # Keep chat history
            conversation_history.append(bot_response)

        # Display chatbot response
        st.write(f"Newbie: {bot_response}")
