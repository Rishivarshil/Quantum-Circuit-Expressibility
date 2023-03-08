# Quantum-Circuit-Expressibility
EXPLORING THE CORRELATION BETWEEN EXPRESSIBILITY AND CLASSIFICATION ACCURACY IN QUANTUM CIRCUITS

## Abstract
An active area of investigation is the intersection of both quantum computing and machine learning. And at the forefront of this new era searching for quantum advantage is “Noisy Intermediate-Scale Quantum” (NISQ) devices. A particular class of algorithms that maximizes the use of such pre-threshold hardware is Parameterized Quantum Circuits in a hybrid of quantum and classical setup promises advancements in accuracy by utilizing the high dimensionality of the Hilbert space as feature space. However, the question remains to be: is the ability to uniformly address the Hilbert space a good descriptor of algorithm performance? In this work, I used work from prior studies to quantify this descriptor of addressing the Hilbert Space, otherwise known as expressibility, and evaluate the correlation between expressibility and the classification accuracy. I then performed classical simulations on various datasets of varying difficulty and calculated a statistical analysis to evaluate the potential relationship. I found that there is no correlation between expressibility and accuracy. Circuit 3 and 4 demonstrate this extremely well as the number of layers and changing expressibility had no effect on the accuracy. Ultimately, this work can serve as a starting point that will give researchers an understanding behind the characteristics associated with an “effective” training circuit.

## Requirements
- Qiskit
- Numpy
- Sklearn
- Matplotlib - Pytorch
- Pandas
- Math

## Setup & Run
In classification.py, set CircuitID to whichever circuit you want to run (circuits are defined in circuits.py). Then run the following command.

```
python3 classification.py
```
