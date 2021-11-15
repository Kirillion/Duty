import numpy as np

#Разборка массива:

def data_array(array):
    
    return np.unique(array,return_index=True,return_counts=True)

#Чудеса матстата:

def search_Mean(array):

    sum = np.sum(array)
    lenght = len(array)

    mean = sum/lenght

    return mean

def search_Expectation(array):

    short_array, array_indexs, array_counts = data_array(array)
    lenght = len(array)

    expectation = np.sum(array_counts/lenght*short_array)

    return expectation
    
def search_Dispersion(array):
    return
def search_Standard_deviation(array):
    return
