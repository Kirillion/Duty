import numpy as np

#Чудеса матстата

def getExpectation(array):

    data,data_count = np.unique(array,return_counts=True)
    
    data_p = data_count/len(data)
    
    return np.sum(data_p*data)

def getDispersion(array):

    dispersion = getExpectation(np.power(array-getExpectation(array),2))
    

    return dispersion

def getStandard_deviation(array):

    standard_deviation = np.power(getDispersion(array),1/2)

    return standard_deviation

#Нормальное распредиление вероятностей

def normal_distribution_density(array, expectation, standard_deviation):

    numerator = np.exp( np.power((array-expectation)/standard_deviation,2)/(-2))
    denumerator = standard_deviation*np.power(2*np.pi,1/2)

    return numerator/denumerator

# Ненормальное распредиление вероятностей (равномерное)

def uniform_distribution_dansity(array,a,b):

    if(array>a and array<b):
        return 1/(b-a)
    elif(array==a or array==b):
        return 1/2*(b-a)
    else :
        return 0

    
