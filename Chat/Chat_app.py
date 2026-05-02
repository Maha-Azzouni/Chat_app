import streamlit as st
import random

st.title("Trial Chat Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm fine and you"
    
    elif "Tell me about you" in user_input:
        return "I'm an trial assistant"
    
    elif "bye" in user_input:
        return "Goodbye!! Thanks for using me"
    
    # Some random responses if the prompt the user did enter dose'nt match the condition
    responses = [
        "This is exiting, tell me about this subject",
        "Rate me from 1 to 10.",
        "Can you explain it in different way?",
        "Let me think",
        "I'm just a simple bot, but I will grow better through the time!"
    ]
    
    return random.choice(responses)


#Display the chat history between the user and system
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    

# Response to the user
prompt = st.chat_input("What is up?")
if prompt:
    # Display user message in chat message box
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add the user response to the message dictionary in session variable
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_response(prompt)
    
    # Display assistant response in chat message box
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to message dictionary in session variable
    st.session_state.messages.append({"role": "assistant", "content": response})