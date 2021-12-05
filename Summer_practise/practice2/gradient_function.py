import numpy as np
from function import sigmoid, add_zero_feature, unpack_params, pack_params
from sigmoid_gradient import sigmoid_gradient

def gradient_function(nn_params, input_layer_size, hidden_layer_size, num_labels,
                  X, Y, lambda_coef):
    # распаковка параметров
    Theta1, Theta2 = unpack_params(
        nn_params, input_layer_size, hidden_layer_size, num_labels)

    # Задание 3.
    # Реализовать функцию ошибки нейронной сети

    # количество примеров
    m = len(X)

    # вычисление отклика нейронной сети
    A1 = np.array(X)
    Z2 = np.dot(A1, Theta1.T)
    A2 = sigmoid(Z2)
    A2 = add_zero_feature(A2)
    Z3 = np.dot(A2, Theta2.T)
    H = sigmoid(Z3)

    # вычисление ошибки
    d3 = H - Y

    d2 =np.dot(d3 , Theta2)[:, 1:] *sigmoid_gradient(Z2)

    D1 = (np.dot(d2.T,A1)/m)
    D2 = (np.dot(d3.T,A2)/m)

    #
    T1 = np.dot((lambda_coef / m) , Theta1[:, 1:])
    T2 = np.dot((lambda_coef / m) , Theta2[:, 1:])

    D1[:, 1:] = D1[:, 1:] + T1
    D2[:, 1:] = D2[:, 1:] + T2


    return pack_params(D1, D2)


