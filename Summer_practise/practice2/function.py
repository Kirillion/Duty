import numpy as np


def sigmoid(z):
    return np.array(1 / (1 + np.exp(-z)))


def add_zero_feature(X, axis=1):
    return np.append(
        np.ones((X.shape[0], 1) if axis else (1, X.shape[1])), X, axis=axis)


def rand_initialize_weights(L_in, L_out):
    epsilon_init = 0.12
    return np.random.rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init


def decode_y(y):
    num_labels = len(np.unique(y))
    return (np.arange(num_labels)[:, np.newaxis] == (y.T - 1)).astype(float).T


def pack_params(Theta1, Theta2):
    return np.concatenate((Theta1.ravel(), Theta2.ravel()))


def unpack_params(params, input_layer_size, hidden_layer_size, num_labels):
    Theta1 = params[:hidden_layer_size * (input_layer_size + 1)].reshape(
        (hidden_layer_size, (input_layer_size + 1)))
    Theta2 = params[hidden_layer_size * (input_layer_size + 1):].reshape(
        (num_labels, (hidden_layer_size + 1)))
    return Theta1, Theta2
