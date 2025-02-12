"""
Handles the chat interface for the QRNG application using Streamlit.

This module manages the chat sidebar, displays chat history, handles user input,
and provides responses based on predefined questions and answers.

Author: Ricard Santiago Raigada García
Date: 02-12-2025
"""
import streamlit as st
import json
import time

with open("src/markdown/qa.json", "r", encoding="utf-8") as file:
    qa_data = json.load(file)

def chat_qrng() -> None:
    """
    Handles the chat interface for the QRNG application using Streamlit.
    This function manages the chat sidebar, displays chat history, handles user input,
    and provides responses based on predefined questions and answers.
    The chat interface includes:
    - A subheader for the chat section.
    - Displaying chat history from the session state.
    - A selection of predefined questions for the user to choose from.
    - Handling user input and appending it to the chat history.
    - Providing responses to the selected or inputted questions.
    The function uses the following session state variables:
    - chat_history: A list of dictionaries containing the chat messages.
    - pending_response: The question or input awaiting a response.
    The function reruns the Streamlit app to update the chat interface after each user interaction.
    Note:
    - The function assumes the existence of a `qa_data` dictionary containing predefined questions and answers.
    - The function uses `st.chat_message`, `st.chat_input`, and other Streamlit components for the chat interface.
    """
    with st.sidebar:
        st.subheader("💬 Chat QRNG")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        if not st.session_state.chat_history:
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": "Hi! I'm still learning and I can't answer open questions. But I can answer these questions:"
            })

        selected_question = None

        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        st.write("**Selecciona una pregunta:**")
        cols = st.columns(len(qa_data["questions"]))

        for i, question in enumerate(qa_data["questions"].keys()):
            if cols[i].button(question):
                selected_question = question
                st.session_state.chat_history.append({"role": "user", "content": selected_question})
                st.session_state["pending_response"] = selected_question
                st.rerun()
        user_input = st.chat_input("Escribe tu pregunta...")

        if selected_question:
            user_input = selected_question

        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.session_state["pending_response"] = user_input
            st.rerun()

        if "pending_response" in st.session_state and st.session_state["pending_response"]:
            time.sleep(0.5)
            user_question = st.session_state["pending_response"]

            if user_question in qa_data["questions"]:
                response = qa_data["questions"][user_question]
            else:
                response = "Hi! I'm still learning and I can't answer open questions. But I can answer these questions:"

            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.session_state["pending_response"] = None
            st.rerun() 