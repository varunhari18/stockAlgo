from multiprocessing.sharedctypes import Value 
import requests
import datetime
from sortVals import *

def getAPIData(symbol):
    url1 = "https://www.alphavantage.co/query?function=MACDEXT&symbol="+symbol+"&interval=daily&series_type=open&apikey=0JHWWC22MJBHM8GP"
    url2 = "https://www.alphavantage.co/query?function=ROC&symbol="+symbol+"&interval=daily&time_period=50&series_type=close&apikey=0JHWWC22MJBHM8GP"
    url3 = "https://www.alphavantage.co/query?function=STOCH&symbol="+symbol+"&interval=daily&apikey=0JHWWC22MJBHM8GP"
    #url4 = "https://www.alphavantage.co/query?function=VWAP&symbol="+symbol+"&interval=15min&apikey=0JHWWC22MJBHM8GP"
    macd = requests.get(url1).json()
    roc = requests.get(url2).json()
    stoch = requests.get(url3).json()
    #vwap2 = requests.get(url4).json()
    #vwap("2021-06-15",vwap2)
    tempScore,mVal,rVal, sVal = getScore(datetime.datetime.today(),macd,roc,stoch)
    return tempScore,mVal,rVal,sVal


def getScore(startDate,macd2,roc2,stoch2):
    mVal = macd(startDate,macd2)
    rVal = roc(startDate,roc2)
    sVal = stoch(startDate,stoch2)  
    sum = mVal + sVal + rVal
    buyString = "Buy"
    sellString = "Sell"
    holdString = "Hold"
    if sum > 8:
        return buyString,mVal,rVal,sVal
    elif sum > 3:
        return holdString,mVal,rVal,sVal
    else:
        return sellString,mVal,rVal,sVal

