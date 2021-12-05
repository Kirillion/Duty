import  function as fun
import numpy as np


def sigmoid_gradient(array):
    return np.array(fun.sigmoid(array)*(1-fun.sigmoid(array)))