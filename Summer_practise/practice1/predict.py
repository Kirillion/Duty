import numpy as np
import sigmoid as sig

def predict (X, Theta1, Theta2):

    ones = np.ones((len(X[:, 1]), 1))
    X = np.c_[ones, X]
    Theta1 = Theta1.T
    Z1 = np.dot(X,Theta1)
    g1 = sig.sigmoid(Z1)

    ones = np.ones((len(g1[:, 1]), 1))
    g1 = np.c_[ones, g1]
    Theta2 = Theta2.T
    Z2 = np.dot(g1, Theta2)
    g2 = sig.sigmoid(Z2)

    return np.argmax(g2,axis=1)+1