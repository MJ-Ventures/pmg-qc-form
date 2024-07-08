import streamlit as st
from PIL import Image
import pandas as pd
import string
import numpy as np
from agent import agent


class ChatbotApp:
    def run(self):
        # set to dark mode
        st.title("Welcome to General Bot")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        for msg in st.session_state.messages:
            print(st.session_state.messages)
            st.chat_message(msg['role']).write(msg.get("content"))
        if prompt := st.chat_input():
            #message = st.chat_input("Message", "")
            print(prompt)
            st.session_state.messages.append({"content": prompt, "role": "user"})
            messages = st.session_state.messages
            st.chat_message("user").write(prompt)
            response = agent(prompt, messages)
            st.session_state.messages.append({"content": response, "role": "assistant"})
            st.chat_message("assistant").write(response)




if __name__ == "__main__":
    app = ChatbotApp()
    app.run()
