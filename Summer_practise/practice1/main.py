import scipy.io as sc
import displayData as DD
import numpy as np
import predict as pr
import matplotlib.pyplot as plt

data_test = sc.loadmat("test_set.mat")
data_weights = sc.loadmat("weights.mat")

X = data_test['X']
y = data_test['y']

Theta1 = data_weights['Theta1']
Theta2 = data_weights['Theta2']

m = len(X)

indexs = np.random.permutation(m)

DD.displayData(X[indexs[:100]])

pred = pr.predict(X,Theta1, Theta2)

#ans = np.mean(np.double(pred == y.ravel()))
#print(ans*100)

plt.figure()
for i in range(5):
    X2 = X[indexs[i],:]
    X2 = np.matrix(X[indexs[i]])
    pred = pr.predict(X2.getA(),Theta1, Theta2)
    pred = np.squeeze(pred)
    pred_str = 'Neural Network Prediction: %d (digit %d)' % (pred, y[indexs[i]])
    DD.displayData(X2, pred_str)
    plt.close()


pred = pr.predict(X,Theta1, Theta2)
ans = np.where(pred != y.ravel())[0]
DD.displayData(X[ans[:100]])








