import numpy as np
from function import sigmoid, add_zero_feature, unpack_params


def cost_function(nn_params, input_layer_size, hidden_layer_size, num_labels,
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
    Z2 = np.dot(A1,Theta1.T)
    A2 = sigmoid(Z2)
    A2 = add_zero_feature(A2)
    Z3 = np.dot(A2,Theta2.T)
    H = sigmoid(Z3)

    # вычисление ошибки
    #J
    J = np.sum(-Y*np.log(H)-(1-Y)*np.log(1-H))/m

    # вычисление регуляризатора
    reg_J =  (np.sum(np.power(Theta1, 2)) + np.sum(np.power(Theta2, 2))) * lambda_coef / ( 2 * m)

    J += reg_J

    return J
