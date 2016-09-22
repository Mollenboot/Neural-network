import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

startdate = "24 09 2011"
enddate = "24 09 2016"
startdate = dt.datetime.strptime(startdate, '%d %m %Y').strftime('%b+%d%%2C+%Y')
enddate = dt.datetime.strptime(enddate, '%d %m %Y').strftime('%b+%d%%2C+%Y')

bedrijven = {"apple": 22144, "netflix": 672501}

url={}

for bedrijf in bedrijven:
    url[bedrijf] = "http://www.google.com/finance/historical?cid=%s&startdate=%s&enddate=%s&num=30&ei=8R7kV4PHEpWRUNSzjuAC&output=csv" %(bedrijven[bedrijf], startdate,enddate)

df_apple = pd.read_csv(url["apple"], index_col="\xef\xbb\xbfDate")


df_apple = df_apple.iloc[::-1]
#df_apple["Volume"].plot()
#
#plt.show()
