from qiskit import *
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import IBMQ, Aer, execute,assemble,QuantumCircuit
from qiskit.visualization import plot_histogram, plot_bloch_vector, plot_bloch_multivector
from qiskit.quantum_info import Statevector
from qiskit.extensions import *

from qiskit.quantum_info import random_unitary

import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import math
from math import pi, sqrt

from scipy.special import rel_entr

from random import seed
from random import random
import cmath
import os

from qiskit.circuit import Parameter
import sys
sys.path.append('../Pyfiles')
from circuits import *
#Possible Bin
bins_list=[];
for i in range(76):
    bins_list.append((i)/75)
#Center of the Bean
bins_x=[]    
for i in range(75):
    bins_x.append(bins_list[1]+bins_list[i])
def P_harr(l,u,N):
    return (1-l)**(N-1)-(1-u)**(N-1)
#Harr historgram
P_harr_hist=[]
for i in range(75):
    P_harr_hist.append(P_harr(bins_list[i],bins_list[i+1],16))
list_of_circuit = [circuit1,circuit6,circuit9,circuit10,circuit14]
backend = Aer.get_backend('qasm_simulator')

arr = []
for kk in range(19):
    arr.append([])
    for lo in [1,2,3,4,5]:
        nshot=1000
        nparam=2000
        fidelity=[]
        for x in range(nparam):
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            qc = QuantumCircuit(qr, cr)

            theta=[];
            for y in range(500):
                theta.append(2*pi*random())

            qc=list_of_circuit[kk](qc,qr,theta,lo,1)


            qc.measure(qr[:],cr[:])
            job = execute(qc, backend, shots=nshot)
            result = job.result()
            count =result.get_counts()

            if '0000' in count and '1' in count:
                ratio=count['0000']/nshot
            elif '0000' in count and '1' not in count:
                ratio=count['0000']/nshot
            else:
                ratio=0

            fidelity.append(ratio)
            
        weights = np.ones_like(fidelity)/float(len(fidelity))
        
        # example of calculating the kl divergence (relative entropy) with scipy
        P_hist=np.histogram(fidelity, bins=bins_list, weights=weights, range=[0, 1])[0]
        kl_pq = rel_entr(P_hist, P_harr_hist)
        arr[kk].append(sum(kl_pq))
        print(kk,'cir',lo,'lay')

np.set_printoptions(threshold=sys.maxsize)
np.savetxt("express_nshot1000_nparam2000.txt",express)

print(express)
