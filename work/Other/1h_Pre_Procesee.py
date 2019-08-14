import datetime
import pandas as pd
import numpy as np
import os
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#实际时间，即从1月1日00时至12月31日23时的一个列表
def historyTureTime():
    timeStr = '2018-01-01-00'
    hisTime = datetime.datetime.strptime(timeStr, '%Y-%m-%d-%H')
    oneHour = datetime.timedelta(hours = 1)
    with open('E:/Rain1hForEveryNStation/2018Time.txt','w') as file1:
        file1.write('Year Mon Day Hour\n')
        file1.write(hisTime.strftime('%Y %m %d %H') + '\n')
        for i in range(365*24):
            now = hisTime + oneHour
            hisTime = now
            file1.write(now.strftime('%Y %m %d %H') + '\n')

def historyTureDateTime():
    timeStr = '2018-01-01'
    hisDateTime = datetime.datetime.strptime(timeStr, '%Y-%m-%d')
    oneDay = datetime.timedelta(days = 1)
    listofDateTime = []
    a = hisDateTime.strftime('%Y%m%d')
    listofDateTime.append(a)
    for i in range(364):
        nowDay = hisDateTime + oneDay
        hisDateTime = nowDay
        days = nowDay.strftime('%Y%m%d')
        listofDateTime.append(days)
    return listofDateTime

def listOfTime():
    listOfTime = []
    for i in range(24):
        listOfTime.append(str(i))
    return listOfTime

def dataProcess(basePath,listOfDate,listOfTime):
    listOfDir = os.listdir(basePath)
    for singleFile in listOfDir:
        print(singleFile)
        df1 = pd.read_table(basePath + singleFile, skiprows=range(0, 2), sep=' ')
        df2 = df1.drop_duplicates(['Year','Mon','Day','Hour'])
        df3 = pd.read_table('E:/Rain1hForEveryNStation/2018Time.txt', sep=' ')
        df4 = pd.merge(df3, df2, how='left', on=['Year', 'Mon', 'Day', 'Hour'])
        df4 = df4.fillna(0.0)
        Pre_1h = df4['PRE_1h']
        dfFinal = pd.DataFrame(np.array(Pre_1h).reshape(365, 24), index=listOfDate, columns=listOfTime)
        dfFinal.to_csv('E:/Rain1hForEveryNStation/'+'2018CSV/'+singleFile[0:-4]+'.CSV')


if __name__ == '__main__':
    basePath = 'E:/Rain1hForEveryNStation/2018/'
    listOfDate = historyTureDateTime()
    listOfTime = listOfTime()
    dataProcess(basePath,listOfDate,listOfTime)
    print('Done')
