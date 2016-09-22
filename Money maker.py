import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from Neural_Network import *

startdate = "24 09 2011"
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

X = [ df_apple[i:-6+i] for i in range(6)]
X = np.array(X).T
print 'Size of df_apple:', X.shape

Y = [df_apple[6:]]
Y = np.array(Y).T
print Y.shape

NN = Neural_Network()
T = trainer(NN)
T.train(X,Y)

# Yhat = NN.forward(X)

# plt.plot(Y)
# plt.plot(Yhat)
# plt.show()
