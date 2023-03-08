import random
from random import seed
from random import random

from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
from matplotlib import pyplot

import numpy as np
import matplotlib.pyplot as plt
from sklearn import mixture
from sklearn.neighbors import KernelDensity

import random

def my_circle(center, rx, ry, Nmax):
    #This function generate the random number inside of the circle
    #center is the location of the circle. input : [x,y]
    # rx is the radius of the eplicipe in x-axis. input : rx
    # ry is the radius of the eplicipe in y-axis. input : ry
    # Total number of the data. input: Nmax
    # Output will generate the data in array{[[x1,y1],[x2,y2]....[xn,yn]]}
    
    x2=[]
    y2=[]
    for i in range(Nmax):
        r2=np.sqrt(random.random())
        theta2=2 * np.pi * random.random()
        x2.append(rx*r2 * np.cos(theta2) + center[0])
        y2.append(ry*r2 * np.sin(theta2) + center[1])

    
    return np.transpose([x2,y2])
def my_plot(data,lab,counter):
    #This function generate the plot of the labeled data
    
    for label, _ in counter.items():
        row_ix = where(lab == label)[0]
        pyplot.scatter(data[row_ix, 0], data[row_ix, 1], label=str(label))
    pyplot.legend()
    pyplot.xlim([0, 1])
    pyplot.ylim([0, 1])
    pyplot.show()

def data0test():
    seed(30)
    X1=my_circle([0.24,0.5],0.2,0.4,750)
    X2=my_circle([0.76,0.5],0.2,0.4,750)
    y1=[0] * 750
    y2=[1] * 750

    X_1=np.concatenate((X1,X2))
    y_1=np.concatenate((y1, y2))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter




def data1a():
    seed(30)
    X1=my_circle([0.3,0.5],0.25,0.4,750)
    X2=my_circle([0.7,0.5],0.25,0.4,750)
    y1=[0] * 750
    y2=[1] * 750

    X_1=np.concatenate((X1,X2))
    y_1=np.concatenate((y1, y2))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter


def data1b():
    seed(30)
    
    X1=my_circle([0.4,0.2],0.25,0.15,375)
    X2=my_circle([0.6,0.5],0.25,0.15,750)
    X3=my_circle([0.4,0.8],0.25,0.15,375)
    y1=[0] * 375
    y2=[1] * 750
    y3=[0] * 375

    X_1=np.concatenate((X1,X2,X3))
    y_1=np.concatenate((y1, y2,y3))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter


def data1c():
    seed(30)
    
    X1=my_circle([0.3,0.2],0.25,0.12,375)
    X2=my_circle([0.7,0.4],0.25,0.12,375)
    X3=my_circle([0.3,0.6],0.25,0.12,375)
    X4=my_circle([0.7,0.8],0.25,0.12,375)
    y1=[0] * 375
    y2=[1] * 375
    y3=[0] * 375
    y4=[1] * 375

    X_1=np.concatenate((X1,X2,X3,X4))
    y_1=np.concatenate((y1, y2,y3,y4))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

def data2a():
    seed(30)
    
    X1=my_circle([0.25,0.25],0.2,0.2,375)
    X2=my_circle([0.25,0.75],0.2,0.2,375)
    X3=my_circle([0.75,0.75],0.2,0.2,375)
    X4=my_circle([0.75,0.25],0.2,0.2,375)
    y1=[0] * 375
    y2=[1] * 375
    y3=[0] * 375
    y4=[1] * 375

    X_1=np.concatenate((X1,X2,X3,X4))
    y_1=np.concatenate((y1, y2,y3,y4))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

def data2b():
    seed(30)
    
    r=0.12
    n=166
    X1=my_circle([0.2,0.2],r,r,n)
    X2=my_circle([0.5,0.2],r,r,n)
    X3=my_circle([0.8,0.2],r,r,n)
    X4=my_circle([0.2,0.5],r,r,n)
    X5=my_circle([0.5,0.5],r,r,n)
    X6=my_circle([0.8,0.5],r,r,n)
    X7=my_circle([0.2,0.8],r,r,n)
    X8=my_circle([0.5,0.8],r,r,n)
    X9=my_circle([0.8,0.8],r,r,n)

    y1=[0] * n
    y2=[1] * n
    y3=[0] * n
    y4=[1] * n
    y5=[0] * n
    y6=[1] * n
    y7=[0] * n
    y8=[1] * n
    y9=[0] * n
    
    X_1=np.concatenate((X1,X2,X3,X4,X5,X6,X7,X8,X9))
    y_1=np.concatenate((y1, y2,y3,y4,y5,y6,y7,y8,y9))


    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

def data2c():
    seed(30)
    
    r=0.1
    n=93
    X1=my_circle([0.15,0.15],r,r,n)
    X2=my_circle([0.38,0.15],r,r,n)
    X3=my_circle([0.62,0.15],r,r,n)
    X4=my_circle([0.85,0.15],r,r,n)
    X5=my_circle([0.15,0.38],r,r,n)
    X6=my_circle([0.38,0.38],r,r,n)
    X7=my_circle([0.62,0.38],r,r,n)
    X8=my_circle([0.85,0.38],r,r,n)
    X9=my_circle([0.15,0.62],r,r,n)
    X10=my_circle([0.38,0.62],r,r,n)
    X11=my_circle([0.62,0.62],r,r,n)
    X12=my_circle([0.85,0.62],r,r,n)
    X13=my_circle([0.15,0.85],r,r,n)
    X14=my_circle([0.38,0.85],r,r,n)
    X15=my_circle([0.62,0.85],r,r,n)
    X16=my_circle([0.85,0.85],r,r,n)

    y1=[0] * n
    y2=[1] * n
    y3=[0] * n
    y4=[1] * n
    y5=[1] * n
    y6=[0] * n
    y7=[1] * n
    y8=[0] * n
    y9=[0] * n
    y10=[1] * n
    y11=[0] * n
    y12=[1] * n
    y13=[1] * n
    y14=[0] * n
    y15=[1] * n
    y16=[0] * n

    X_1=np.concatenate((X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16))
    y_1=np.concatenate((y1, y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

def data3a():
    seed(30)
    
    X1 = []
    radius = 0.25
    n=750

    index = 0
    while index < n:
        x=random.random()
        y=random.random()
        if (x-0.5)**2 + (y-0.5)**2 > radius**2:
            X1 = X1 + [[x,y]]
            index = index + 1
    
    y1=[1] *750
    X2=my_circle([0.5,0.5],radius,radius,750)

    y2=[0] *750

    X_1=np.concatenate((X1,X2))
    y_1=np.concatenate((y1, y2))


    # Generate uniform noise
    counter = Counter(y_1)


    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

def data3b():
    seed(30)
    
    X1 = []
    radius = 0.15
    n=750

    index = 0
    while index < n:
        x=random.random()
        y=random.random()
        if ((x-0.25)**2 + (y-0.25)**2 > radius**2 and (x-0.75)**2 + (y-0.75)**2 > radius**2):
            X1 = X1 + [[x,y]]
            index = index + 1
    
    y1=[1] *750

    X2=my_circle([0.25,0.25],radius,radius,375)
    X3=my_circle([0.75,0.75],radius,radius,375)

    y2=[0] *750

    X_1=np.concatenate((X1,X2,X3))
    y_1=np.concatenate((y1, y2))

    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

def data3c():
    seed(30)
    
    X1 = []
    radius = 0.15
    n=750
    n2=187
    index = 0
    while index < n:
        x=random.random()
        y=random.random()
        if ((x-0.25)**2 + (y-0.25)**2 > radius**2 and (x-0.75)**2 + (y-0.75)**2 > radius**2 and (x-0.75)**2 + (y-0.25)**2 > radius**2 and (x-0.25)**2 + (y-0.75)**2 > radius**2 ):
            X1 = X1 + [[x,y]]
            index = index + 1
    
    y1=[1] *748

    X2=my_circle([0.25,0.25],radius,radius,n2)
    X3=my_circle([0.75,0.75],radius,radius,n2)
    X4=my_circle([0.75,0.25],radius,radius,n2)
    X5=my_circle([0.25,0.75],radius,radius,n2)

    y2=[0] *748

    X_1=np.concatenate((X1,X2,X3,X4,X5))
    y_1=np.concatenate((y1, y2))


    # Generate uniform noise
    counter = Counter(y_1)


    # Generate uniform noise
    counter = Counter(y_1)
    
    return X_1, y_1, counter

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

np.savetxt("data1a.txt",data1a()[0],fmt='%.2f')
np.savetxt("data1b.txt",data1b()[0],fmt='%.2f')
np.savetxt("data1c.txt",data1c()[0],fmt='%.2f')
np.savetxt("data2a.txt",data2a()[0],fmt='%.2f')
np.savetxt("data2b.txt",data2b()[0],fmt='%.2f')
np.savetxt("data2c.txt",data2c()[0],fmt='%.2f')
np.savetxt("data3a.txt",data3a()[0],fmt='%.2f')
np.savetxt("data3b.txt",data3b()[0],fmt='%.2f')
np.savetxt("data3c.txt",data3c()[0],fmt='%.2f')

np.savetxt("data1alabel.txt",data1a()[1],fmt='%.2f')
np.savetxt("data1blabel.txt",data1b()[1],fmt='%.2f')
np.savetxt("data1clabel.txt",data1c()[1],fmt='%.2f')
np.savetxt("data2alabel.txt",data2a()[1],fmt='%.2f')
np.savetxt("data2blabel.txt",data2b()[1],fmt='%.2f')
np.savetxt("data2clabel.txt",data2c()[1],fmt='%.2f')
np.savetxt("data3alabel.txt",data3a()[1],fmt='%.2f')
np.savetxt("data3blabel.txt",data3b()[1],fmt='%.2f')
np.savetxt("data3clabel.txt",data3c()[1],fmt='%.2f')
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

np.savetxt("data1a.txt",data1a()[0],fmt='%.2f')
np.savetxt("data1b.txt",data1b()[0],fmt='%.2f')
np.savetxt("data1c.txt",data1c()[0],fmt='%.2f')
np.savetxt("data2a.txt",data2a()[0],fmt='%.2f')
np.savetxt("data2b.txt",data2b()[0],fmt='%.2f')
np.savetxt("data2c.txt",data2c()[0],fmt='%.2f')
np.savetxt("data3a.txt",data3a()[0],fmt='%.2f')
np.savetxt("data3b.txt",data3b()[0],fmt='%.2f')
np.savetxt("data3c.txt",data3c()[0],fmt='%.2f')

np.savetxt("data1alabel.txt",data1a()[1],fmt='%.2f')
np.savetxt("data1blabel.txt",data1b()[1],fmt='%.2f')
np.savetxt("data1clabel.txt",data1c()[1],fmt='%.2f')
np.savetxt("data2alabel.txt",data2a()[1],fmt='%.2f')
np.savetxt("data2blabel.txt",data2b()[1],fmt='%.2f')
np.savetxt("data2clabel.txt",data2c()[1],fmt='%.2f')
np.savetxt("data3alabel.txt",data3a()[1],fmt='%.2f')
np.savetxt("data3blabel.txt",data3b()[1],fmt='%.2f')
np.savetxt("data3clabel.txt",data3c()[1],fmt='%.2f')
