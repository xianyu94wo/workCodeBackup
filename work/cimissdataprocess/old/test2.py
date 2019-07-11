import numpy as np
import os
import pandas as pd
#设置文件路径
oneStationDataFilePath = "I:\\2018pre\\cimissdataprocess\\2018_pre_test\\"
stationFilePath =  "I:\\2018pre\\cimissdataprocess\\2018_Station_ID.txt"
baseFile = "I:\\2018pre\\cimissdataprocess\\base.csv"
#将CIMISS下载的数据中的时间格式化
with open(stationFilePath) as file1:
    list1 = file1.readlines()
    for file in range(len(list1)):
        stationId = list1[file].strip("\n")
        oneStationDataFile = oneStationDataFilePath + "new_"+stationId + ".txt"
        oldAry = np.loadtxt(oneStationDataFile, dtype=np.float)
        listIndex = []
        for i in range(oldAry.shape[0]):
            indexA = str(int(oldAry[i][0]))
            indexB = (str(int(oldAry[i][1]))).zfill(2)
            indexC = (str(int(oldAry[i][2]))).zfill(2)
            indexD = (str(int(oldAry[i][3]))).zfill(2)
            indexE = (str(oldAry[i][4]))
            indexALL = indexA + "-" + indexB + "-" + indexC + " " + indexD + ":00:00 " + indexE
            listIndex.append(indexALL)
# 将格式化后的时间标签写入每个新csv文件中
        listIndex2 = []
        for j in listIndex:
            listIndex2.append(j.split())
        dfTurn = pd.DataFrame(np.array(listIndex2),columns = ["Date","Time",stationId])
#按Date和Time删除重复项
        dfTurn2 = dfTurn.drop_duplicates(['Date', 'Time'])
        dfTurn2.to_csv(oneStationDataFilePath + stationId + ".csv",index=0)
#合并每个文件到base文件
        fo1 = open(oneStationDataFilePath + stationId + ".csv")
        df1 = pd.read_csv(fo1, index_col=['Date', 'Time'])
        fo2 = open(baseFile)
        df2 = pd.read_csv(fo2, index_col=['Date', 'Time'])
        newDf = pd.concat([df2,df1],axis=1)
#缺省值NaN填充为0
        newDf = newDf.fillna(0.0)
        newDf.to_csv(baseFile)
        fo1.close()
        fo2.close()
print("Done!")




