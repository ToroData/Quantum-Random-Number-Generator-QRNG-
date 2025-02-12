from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from qiskit import transpile
from qiskit.circuit.library import HGate, MCXGate, XGate, ZGate
from qiskit.visualization import plot_bloch_multivector, visualize_transition
from matplotlib import pyplot as plt
from qiskit_aer.library import save_statevector
from qiskit.quantum_info import partial_trace

from qiskit.visualization import plot_histogram, plot_distribution
from qiskit_aer import AerSimulator, QasmSimulator
from qiskit.quantum_info import Statevector



def create_circuit(n_bits: int) -> QuantumCircuit:
    qc = QuantumCircuit(n_bits)
    for q in range(n_bits):
        qc.h(q)
    return qc

def circuit_visualization(qc):
    return qc.draw('mpl')


def bloch_sphere(qc):
    simulator = AerSimulator(method='statevector')
    return plot_bloch_multivector(Statevector(qc))


def transition(qc):
    """_summary_

    Args:
        qc (_type_): _description_

    Returns:
        _type_: _description_
    """
    return visualize_transition(qc, saveas='movie.gif')


def simulate_circuit(qc, n_shots=1):
    qc.measure_all()
    simulator = AerSimulator(method='automatic')
    qc_transpiled = transpile(qc, simulator)
    result = simulator.run(qc_transpiled, shots=n_shots).result()
    counts = result.get_counts()
    bitstring = list(counts.keys())[0]
    return bitstring.zfill(qc.num_qubits)


def split_into_chunks(bitstring, chunk_size=4):
    bitstring = bitstring.zfill(((len(bitstring) + chunk_size - 1) // chunk_size) * chunk_size)
    return [bitstring[i:i + chunk_size] for i in range(0, len(bitstring), chunk_size)]

def convert_to_decimal(bit_chunks):
    return [int(chunk, 2) for chunk in bit_chunks]
