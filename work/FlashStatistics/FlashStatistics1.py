import pandas as pd
import os
import numpy as np

def singleFileSplice(filePath0,resultPath):
    fileList1 = os.listdir(filePath0)
    for i in fileList1:
        dfBase = pd.read_table('E:/DATA/dfbase.txt', encoding='gb2312', sep='   ', header=None, engine='python')
        filePath2 = filePath0 + i + '/'
        fileList2 = os.listdir(filePath2)
        for j in fileList2:
            filePath3 = filePath2 + j + '/'
            fileList3 = os.listdir(filePath3)
            for k in fileList3:
                filePath = filePath3 + k
                print(filePath)
                dfTemp = pd.read_table(filePath, encoding='gb2312', sep='   ', header=None, engine='python')
                dfBase = pd.concat([dfBase,dfTemp])
        dfBase.to_csv(resultPath+i+'.txt', encoding='gb2312')
    return None

def StationClassify(resultPath):
    with open('E:/DATA/县.txt', 'r', encoding='UTF-8') as fileCounty:
        list1 = fileCounty.readlines()
        list2 = os.listdir(resultPath)
        for i in list1:
            i1 = i.strip('\n')
            for j in list2:
                tempPath = resultPath + j
                dfTemp = pd.read_table(tempPath, encoding='gb2312', sep=',', header=None, engine='python')
                dfTemp = dfTemp.drop(columns=[0, 1]).drop(index=[0, 1])
                dfTemp.columns = ['日期', '时间', '纬度', '经度', '强度', '陡度', '误差', '定位方式', '省', '市', '县']
                dfTemp = dfTemp[dfTemp['县'].isin([i1])]
                dfTemp = dfTemp.drop_duplicates()
                dfTemp.to_csv('E:/FlashStatistics各县逐年/' + j[0:4] + i1[2:] + '.txt', encoding='gb2312')
                print(dfTemp)
                print('Done Now!')


if __name__ == '__main__':
    resultPath = 'E:/FlashStatistics/'
    #a = singleFileSplice(filePath0,resultPath)
    StationClassify(resultPath)
    print('ALL DONE!')






