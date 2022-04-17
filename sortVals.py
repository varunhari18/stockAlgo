from multiprocessing.sharedctypes import Value
import datetime
import numpy as np
import pandas as pd


#this file contains all functions related to looking at individual metrics for a given stock and assigning scores
def vwap(startDate,data):
    print(data) 

def macd(startDate,data):

    #print(startDate)
    format2 = '%Y-%m-%d'
    start = startDate
    timeDelt = datetime.timedelta(days=9)
    end = start - timeDelt
    
    data2 = data['Technical Analysis: MACDEXT']
    macdArray = []
    signalArray = []
    dateArray = []
    timeDict = list(data2.keys())
    valDict = list(data2.values())

    for x in valDict:
        macdArray.append(float(x['MACD']))
        signalArray.append(float(x['MACD_Signal']))

    for input in timeDict:
        format = '%Y-%m-%d'
        try:
            newVal = datetime.datetime.strptime(input, format)
            dateArray.append(newVal)
        except ValueError:
            continue

    dateArray2 = []
    macdArray2 = []
    signalArray2 = []

    for x in range(len(dateArray)):
        if dateArray[x] < start and dateArray[x] > end:
            dateArray2.append(dateArray[x])
            macdArray2.append(macdArray[x])
            signalArray2.append(signalArray[x])
    macdNum = np.array(macdArray2)
    df = pd.DataFrame({'Stock_Values': macdNum})
    ema = df.ewm(span=10, adjust=True).mean()


    if macdArray2[-1] > ema.last_valid_index():
        return 3
    else:
        return 0

def roc(startDate, data):
    format2 = '%Y-%m-%d'
    currDate = startDate

    data2 = data['Technical Analysis: ROC']
    rocArray=[]
    dateArray = []
    timeDict = list(data2.keys())
    valDict = list(data2.values())

    for x in valDict:
        rocArray.append(float(x['ROC']))
    for input in timeDict:
        format = '%Y-%m-%d'
        try:
            newVal = datetime.datetime.strptime(input, format)
            dateArray.append(newVal)
        except ValueError:
            continue
    dateArray2 = []
    roc2 = []
    dateROC = -5
    for x in range(len(dateArray)):
        if dateArray[x] == currDate:
            #print(dateArray[x].strftime(format2))

            dateROC = rocArray[x]
            
    if dateROC > 1:
        return 3
    elif dateROC > -1 and dateROC <= 1:
        return 1.5
    else:
        return 0

def stoch(startDate, data):
    format2 = '%Y-%m-%d'
    currDate = startDate
    #print(prevDate.strftime(format2))
    #end = datetime.datetime.strptime(endDate, format2)
    data2 = data['Technical Analysis: STOCH']


    slowK = []
    slowD = []
    dateArray = []
    timeDict = list(data2.keys())
    valDict = list(data2.values())

    for x in valDict:
        slowK.append(float(x['SlowK']))
        slowD.append(float(x['SlowD']))

    for input in timeDict:
        format = '%Y-%m-%d'
        try:
            newVal = datetime.datetime.strptime(input, format)
            dateArray.append(newVal)
        except ValueError:
            continue

    dateArray2 = []
    slowK2 = []
    slowD2 = []

    dateSlowK = -100
    for x in range(len(dateArray)):
        if dateArray[x] == currDate:
            #dateArray2.append(dateArray[x])
            dateSlowK=slowK[x]
            slowD2.append(slowD[x])

    if dateSlowK < 20:
        return 3
    elif dateSlowK < 80 and dateSlowK > 20:
        return 1.5
    else:
        return 0