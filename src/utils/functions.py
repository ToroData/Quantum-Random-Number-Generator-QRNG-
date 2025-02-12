"""
This module provides utility functions for creating and visualizing quantum circuits,
as well as simulating and processing the results of quantum computations.

Functions:
- create_circuit(n_bits: int) -> QuantumCircuit:
    Creates a quantum circuit with the specified number of qubits, applying a Hadamard gate to each qubit to create a superposition state.

- circuit_visualization(qc: QuantumCircuit):
    Visualizes a quantum circuit using Matplotlib.

- bloch_sphere(qc: QuantumCircuit):
    Plots the Bloch sphere representation of a given quantum circuit.

- transition(qc: QuantumCircuit):
    Visualizes the transition of a quantum circuit and saves it as a GIF.

- simulate_circuit(qc: QuantumCircuit, n_shots: int = 1) -> str:
    Simulates a quantum circuit using the AerSimulator and returns the resulting bitstring.

- split_into_chunks(bitstring: str, chunk_size: int = 4) -> list:
    Splits a bitstring into chunks of a specified size, padding with leading zeros if necessary.

- convert_to_decimal(bit_chunks: list) -> list:
    Converts a list of binary string chunks to their decimal equivalents.

Author: Ricard Santiago Raigada García
Date: 02-12-2025
"""
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.visualization import plot_bloch_multivector, visualize_transition
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector


def create_circuit(n_bits: int) -> QuantumCircuit:
    """
    Creates a quantum circuit with the specified number of qubits, 
    applying a Hadamard gate to each qubit to create a superposition state.

    Args:
        n_bits (int): The number of qubits in the quantum circuit.

    Returns:
        QuantumCircuit: A quantum circuit with Hadamard gates applied to each qubit.
    """
    qc = QuantumCircuit(n_bits)
    for q in range(n_bits):
        qc.h(q)
    return qc

def circuit_visualization(qc):
    """
    Visualizes a quantum circuit using Matplotlib.

    Args:
        qc (QuantumCircuit): The quantum circuit to be visualized.

    Returns:
        matplotlib.figure.Figure: A Matplotlib figure object representing the quantum circuit.
    """
    return qc.draw('mpl')


def bloch_sphere(qc):
    """
    Plots the Bloch sphere representation of a given quantum circuit.

    Args:
        qc (QuantumCircuit): The quantum circuit to be visualized on the Bloch sphere.

    Returns:
        matplotlib.figure.Figure: A matplotlib figure object representing the Bloch sphere.
    """
    simulator = AerSimulator(method='statevector')
    return plot_bloch_multivector(Statevector(qc))


def transition(qc):
    """
    Visualizes the transition of a quantum circuit and saves it as a GIF.

    Args:
        qc (QuantumCircuit): The quantum circuit to visualize.

    Returns:
        None
    """
    return visualize_transition(qc, saveas='movie.gif')


def simulate_circuit(qc, n_shots=1):
    """
    Simulates a quantum circuit using the AerSimulator and returns the resulting bitstring.

    Args:
        qc (QuantumCircuit): The quantum circuit to simulate.
        n_shots (int, optional): The number of shots to run the simulation. Defaults to 1.

    Returns:
        str: The resulting bitstring from the simulation, zero-padded to match the number of qubits in the circuit.
    """
    qc.measure_all()
    simulator = AerSimulator(method='automatic')
    qc_transpiled = transpile(qc, simulator)
    result = simulator.run(qc_transpiled, shots=n_shots).result()
    counts = result.get_counts()
    bitstring = list(counts.keys())[0]
    return bitstring.zfill(qc.num_qubits)


def split_into_chunks(bitstring, chunk_size=4):
    """
    Splits a bitstring into chunks of a specified size, padding with leading zeros if necessary.

    Args:
        bitstring (str): The bitstring to be split into chunks.
        chunk_size (int, optional): The size of each chunk. Defaults to 4.

    Returns:
        list: A list of bitstring chunks of the specified size.
    """
    bitstring = bitstring.zfill(((len(bitstring) + chunk_size - 1) // chunk_size) * chunk_size)
    return [bitstring[i:i + chunk_size] for i in range(0, len(bitstring), chunk_size)]

def convert_to_decimal(bit_chunks):
    """
    Convert a list of binary string chunks to their decimal equivalents.

    Args:
        bit_chunks (list of str): A list of binary string chunks.

    Returns:
        list of int: A list of integers representing the decimal equivalents of the binary chunks.
    """
    return [int(chunk, 2) for chunk in bit_chunks]
