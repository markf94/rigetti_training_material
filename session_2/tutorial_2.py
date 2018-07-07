#!pip install qutip

import os

API_KEY = 'YOUR API KEY GOES HERE'
USER_ID = 'YOUR USER ID GOES HERE'

PYQUIL_CONFIG = f"""
[Rigetti Forest]
url: https://api.rigetti.com/qvm
key: {API_KEY}
user_id: {USER_ID}
"""

import numpy
import cmath
from pyquil.quil import Program
from pyquil.api import QVMConnection
from qutip import Bloch

#with open(os.path.expanduser('~/.pyquil_config'), 'w') as f:
#  f.write(PYQUIL_CONFIG)


def get_vector(alpha, beta):
    """
    Function to compute 3D Cartesian coordinates
    from 2D qubit vector.
    """

    # get phases
    angle_alpha = cmath.phase(alpha)
    angle_beta = cmath.phase(beta)

    if (angle_beta < 0 and angle_alpha < angle_beta) or (angle_beta > 0 and angle_alpha > angle_beta):
            denominator = cmath.exp(1j*angle_beta)
    else:
            denominator = cmath.exp(1j*angle_alpha)

    # eliminate global phase
    alpha_new = alpha/denominator
    beta_new = beta/denominator

    # special case to avoid division by zero
    if abs(alpha) == 0 or abs(beta) == 0:
        if alpha == 0:
            return [0,0,-1]
        else:
            return [0,0,1]
    else:
        # compute theta and phi from alpha and beta
        theta = 2*cmath.acos(alpha_new)
        phi = -1j*cmath.log(beta_new/cmath.sin(theta/2))

        # compute the Cartesian coordinates
        x = cmath.sin(theta)*cmath.cos(phi)
        y = cmath.sin(theta)*cmath.sin(phi)
        z = cmath.cos(theta)

    return [x.real,y.real,z.real]

def plot_quantum_state(sphere, amplitudes):
    """
    Thin function to abstract the plotting on the Bloch sphere.
    """
    vec = get_vector(amplitudes[0], amplitudes[1])
    bloch_sphere.add_vectors(vec)
    bloch_sphere.show()
    bloch_sphere.clear()

# Rotations on the Bloch sphere

bloch_sphere = Bloch()
qvm = QVMConnection()

# Rigetti initializes their qubits in the |0> state. This qubit state can be visualized
# on the Bloch sphere as follows:

p = Program()
p.measure(0, 0)
# TODO: make them find out how to get the wavefunction + amplitudes by themselves
amplitudes = qvm.wavefunction(p).amplitudes
#plot_quantum_state(bloch_sphere, amplitudes)

# show off the wavefunction functionalities like plot, pretty_print and probabilities
# of course this only works for small numbers of qubits!

# Exercise: Explore the Pauli gates on the Bloch sphere

# TODO: let them import the gates
from pyquil.gates import I, X, Y, Z

p = Program()
# this is how we apply a NOT gate to qubit 0:
p.inst(X(0))

amplitudes = qvm.wavefunction(p)
#plot_quantum_state(bloch_sphere, amplitudes)

# e.g. H
from pyquil.gates import H
p = Program()
p.inst(H(0))

qvm.wavefunction(p).plot()
amplitudes = qvm.wavefunction(p).amplitudes
plot_quantum_state(bloch_sphere, amplitudes)

# Exercise: Try out T and S and their complex conjugates.

# Introduce parametric gates + np.kron for multi-qubit gates

# Show them different possibilities of chaining instructions

from pyquil.gates import MEASURE
print("Multiple inst arguments with final measurement:")
print(Program().inst(X(0), Y(1), Z(0)).measure(0, 1))

print("Chained inst with explicit MEASURE instruction:")
print(Program().inst(X(0)).inst(Y(1)).measure(0, 1).inst(MEASURE(1, 2)))

print("A mix of chained inst and measures:")
print(Program().inst(X(0)).measure(0, 1).inst(Y(1), X(0)).measure(0, 0))

print("A composition of two programs:")
print(Program(X(0)) + Program(Y(0)))

# Exercise: Let them figure out how to pop instructions

# Exercise: Implement custom single-qubit rotations with pyQuil!

# Exercise: Can you rotate the Bloch vector to these specific locations?

# Exercise: What rotation around which axes does the Hadamard gate result in?

# Manually simplifying circuit with gate identities
# TODO: Use Isaac Chuang's library to draw circuits!

# Flipping CNOTs with Hadamards
# What if we are only allowed to do one-directional CNOTs?
