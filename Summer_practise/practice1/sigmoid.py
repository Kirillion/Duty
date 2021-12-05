import  numpy as np

def sigmoid (Z):
    numerator = 1
    denominator = 1 + np.exp(-Z)
    return numerator/denominator