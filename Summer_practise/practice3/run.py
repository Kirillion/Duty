import function as f
import generator as g
import numpy as np
import matplotlib.pyplot as plt




def norm():
    X = g.getNormsl(200000)
    expectation = f.getExpectation(X)

    standard_deviation = f.getStandard_deviation(X)

    X1 = np.unique(X)

    a = f.normal_distribution_density(X1,expectation,standard_deviation)

    print (expectation)
    print(standard_deviation**2)

    plt.plot(X1, a)
    plt.show()

def unnorm(count,a,b):
    X = g.getUniform(count,a,b)
    P = []
    X = np.unique(X)
    for i in range (len(X)):

       P.append( f.uniform_distribution_dansity(X[i],a,b))

    print(X)
    plt.plot(X, P)
    plt.show()

