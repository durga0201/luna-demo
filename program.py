from typing import Any

from qiskit_ibm_runtime.program import UserMessenger, ProgramBackend
from qiskit import transpile
from qiskit.circuit.random import random_circuit
from numpy import random

def circuit(backend: ProgramBackend, user_messenger: UserMessenger, **kwargs):
    
    c = random_circuit(
        num_qubits=5, depth=4, measure=True, seed=random.randint(0, 1000)
    )
    return transpile(c, backend)

def main(backend: ProgramBackend, user_messenger: UserMessenger, **kwargs) -> Any:
    iterations = kwargs.pop("iterations", 5)
    for it in range(iterations):
        qc = circuit(backend, user_messenger)
        result = backend.run(qc).result()
        user_messenger.publish({"iteration": it, "counts": result.get_counts()})

    return "Done."