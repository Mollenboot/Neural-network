import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import scipy as sp
from scipy.signal import savgol_filter
from Neural_Network import *

startdate = "24 09 2014"
enddate = "24 09 2016"
startdate = dt.datetime.strptime(startdate, '%d %m %Y').strftime('%b+%d%%2C+%Y')
enddate = dt.datetime.strptime(enddate, '%d %m %Y').strftime('%b+%d%%2C+%Y')

bedrijven = {"apple": 22144, "netflix": 672501}

url={}

for bedrijf in bedrijven:
    url[bedrijf] = "http://www.google.com/finance/historical?cid={0}&startdate={1}&enddate={2}&num=30&ei=8R7kV4PHEpWRUNSzjuAC&output=csv".format(bedrijven[bedrijf], startdate,enddate)

df_apple = pd.read_csv(url["apple"], index_col="\xef\xbb\xbfDate")


df_apple = df_apple.iloc[::-1]

df_apple = df_apple["Open"]

df_apple = savgol_filter(df_apple, 101, 2)

X = [ df_apple[i:-6+i] for i in range(6)]
X = np.array(X).T
print 'Size of df_apple:', X.shape



Y = [df_apple[6:]]
Y = np.array(Y).T
print Y.shape


# X = np.array(([3,5,6,8,1,2], [5,1,10,4,3,7], [10,2,3,5,6,8]), dtype=float)
# Y = np.array(([75], [82], [93]), dtype=float)

# # Normalize
# X = X/np.amax(X, axis=0)
# Y = Y/100 #Max test score is 100

NN = Neural_Network()
T = trainer(NN)
T.train(X,Y)

Yhat = NN.forward(X)

plt.plot(Y, 'o')
plt.plot(Yhat,'*')
plt.plot(Yhat - Y,'D')
plt.show()
