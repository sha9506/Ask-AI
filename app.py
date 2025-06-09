import streamlit as st
import openai
import os

# Set your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Ask AI Assistant", page_icon="🤖")

st.title("🤖 Ask the AI Assistant")
st.write("Enter a question or message below and get a smart reply!")

user_input = st.text_input("Your message:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
            )
            # For OpenAI Python SDK v1.x
            reply = response.choices[0].message.content
            st.success("AI says:")
            st.write(reply)
        except Exception as e:
            st.error(f"Error: {e}")
