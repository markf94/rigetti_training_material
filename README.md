# Rigetti Training Day I
This repository contains all necessary material for the first Rigetti training day at the [Creative Destruction Lab Quantum Machine Learning](https://www.creativedestructionlab.com/streams/quantum2018/) stream 2018/2019.

The training was organised by [Rigetti Computing](https://www.rigetti.com/) and jointly conducted by [Tomas Babej](https://www.linkedin.com/in/tbabej/) and [Mark Fingerhuth](https://www.linkedin.com/in/mark-fingerhuth/).

## Timetable

### 900 - 915
Introduction by Peter Wittek

### 915 - 1000
Lecture I: Introduction to universal quantum computing

- Intro to Rigetti
	- Forest
	- Quil
	- pyQuil
	- Grove
	- Quantum Virtual Machine
- First Quil program (quantum assembler)

### 1000 - 1030
Tutorial I: Quantum assembler

- Coding in low-level Quil
- First quantum circuits
- Measuring quantum states

### 1030 - 1045
Coffee break

### 1045 - 1100
Lecture II: Quantum gates & notation
- Visualizing quantum states on the Bloch sphere
- Elementary quantum gates
- Single- and multi-qubit gates
- (Non)equivalence of different notations
- Quantum gate identities

### 1100 - 1200
Tutorial II: Quantum gates on the Bloch sphere
- Pauli gates and arbitrary rotations on the Bloch sphere?
- Manually simplifying quantum circuits
- Flipping CNOTs by sandwiching them with Hadamards

### 1200 - 1230
Lecture III: pyQuil + Abstract quantum programming
- pyQuil syntax & code examples
- how to use the library
- Compiler, QPU and QVM

### 1230 - 1300
Lunch

### 1300 - 1400
Tutorial III: Shallow circuits in pyQuil
- Gate decomposition
- Manual state preparation
- Quantum simulation circuits

### 1400 - 1415
Lecture IV: Rigetti's QPU + Implications
- Rigetti's quantum processor
- Qubit decoherence + noise
- Simulating the QPU with noise models
- QPU topology and implications (SWAPs, "graph embeddings")

### 1415 - 1500
Tutorial IV: Programming the QPU
- Working with noise models
- Finding manual embeddings onto the native QPU topology (minimizing SWAPs)
- Calculating fidelity of circuits
- Using Rigetti's compiler

### 15:00
Coffee break & end
