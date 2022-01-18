import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    e_x=np.exp(x)
    return e_x/np.sum(e_x, axis=0)