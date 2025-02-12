"""
Main script for the Quantum Random Number Generator (QRNG) application using Streamlit.
This script sets up the Streamlit interface, loads configuration data, and integrates
quantum logic visualization and chat functionalities.

Author: Ricard Santiago Raigada García
Date: 02-12-2025
"""
import streamlit as st
import src.sections.quantum_logic_streamlit as quantum
import src.sections.chat as chat
import src.config as config
import src.utils.functions
import json

# Load texts and QA data
texts = config.load_texts()
qa_data = config.load_questions()

# Title
st.set_page_config(page_title="QRNG", page_icon="🔬", layout="wide")
st.title(texts["title"])

# First Section
show_visuals: bool = st.toggle(texts["visual_toggle"], value=True)
n_bits: int = st.slider("Number of Qubits", 2, 30, 4)

# Second Section
quantum.quantum_visualization(n_bits, show_visuals, texts)
quantum.generate_key(n_bits, texts)

# Chat Section
chat.chat_qrng()
