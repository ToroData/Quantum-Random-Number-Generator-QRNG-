"""
This module provides Streamlit-based visualizations and key generation for quantum logic.

Author: Ricard Santiago Raigada García
Date: 02-12-2025
"""
import streamlit as st
from src.utils import functions


def quantum_visualization(n_bits: int, show_visuals: bool, texts: dict) -> None:
    """
    Visualizes quantum states using Bloch sphere and transition images.
    Parameters:
    n_bits (int): Number of qubits to visualize. Visualization is shown only if n_bits is less than or equal to 10.
    show_visuals (bool): Flag to determine whether to show visualizations.
    texts (dict): Dictionary containing text elements for the visualizations. 
                  Expected keys are "visual_bloch", "visual_transition", and "visual_transition_caption".
    Returns:
    None
    """
    if show_visuals and n_bits <= 10:
        st.write(texts["visual_bloch"])
        st.pyplot(functions.bloch_sphere(functions.create_circuit(n_bits=n_bits)), use_container_width=True)

        st.write(texts["visual_transition"])
        st.image("img/movie.gif", caption=texts["visual_transition_caption"], use_container_width=True)
    
def generate_key(n_bits: int, texts: dict) -> None:
    """
    Generates a quantum key and displays it in various formats using Streamlit.
    Args:
        n_bits (int): The number of bits for the quantum key.
        texts (dict): A dictionary containing text for headers and descriptions to be displayed in the Streamlit app.
    Returns:
        None
    """
    qc = functions.create_circuit(n_bits)
    bitstring = functions.simulate_circuit(qc)
    bit_chunks = functions.split_into_chunks(bitstring)
    decimal_values = functions.convert_to_decimal(bit_chunks)

    st.subheader(texts["key_header"])
    if st.toggle(texts["key_header_toggle"], value=True):
        st.markdown(texts["key_desc"])
    st.code(bitstring, language="plaintext")

    st.subheader(texts["datagram_header"])
    if st.toggle(texts["datagram_header_desc"], value=True):
        st.markdown(texts["datagram_desc"])
    st.code(" | ".join(bit_chunks), language="plaintext")

    st.subheader(texts["decimal_header"])
    if st.toggle(texts["decimal_header_desc"], value=True):
        st.markdown(texts["decimal_desc"])
    st.code(" - ".join(map(str, decimal_values)), language="plaintext")
