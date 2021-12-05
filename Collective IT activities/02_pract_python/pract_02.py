import numpy as np
import random as rand

#Ex. 1
def Ex1():

    array1 = np.random.randint(-100, 100, 10)
    array2 = np.random.randint(-100, 100, 10)
    array3 = [num for num in np.abs(array1 - array2) ]

    print (array1)
    print (array2)
    print (array3)

    return 0

#Ex. 7
def Fibonacci(finish_num, array_num):

    lenght = len(array_num)   

    array_num = np.append(array_num, array_num[lenght-1]+array_num[lenght-2])
    print(array_num)

    if(finish_num<array_num[-1]):
        return array_num
    else: Fibonacci(finish_num, array_num)



def Ex2():

    print("Введите число, на котором остановить вычисление:")
    ans = int(input())

    array_num = np.array([0,1])

    print(Fibonacci(ans,array_num))

    return 0

#Ex. 10
def Ex10():

    array1 = np.array([rand.randrange(-100,100) for i in range(10)])
    print(array1)

    min_max = array1.min(),array1.max()
    print(min_max)

    return 0