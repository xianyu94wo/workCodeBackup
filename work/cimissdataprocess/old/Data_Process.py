import numpy as np
import pandas as pd
import datetime
#设置目录
oneStationDataFilePath = "E:\\workspace\\work\\work\\cimissdataprocess\\2018_pre\\"
stationFilePath =  "E:\\workspace\\work\\work\\cimissdataprocess\\2018_Station_ID.txt"
#将世界时改为北京时，输出一个timeList
with open(oneStationDataFilePath+"new_time.txt","r") as timeFile:
    timeData = pd.read_csv(timeFile, sep=' ', engine = 'python', encoding="gbk" )
    timeInfo = np.array(timeData.iloc[:, 0:4])
    deltaTime = datetime.timedelta(hours=8)
    timeList = []
    b1 = np.empty(1, dtype="str")
    for i in range(timeInfo.shape[0]):
        timeBJT = datetime.datetime.strptime(str(timeInfo[i]), "[%Y    %m    %d    %H]") + deltaTime
        timeBJTStr = timeBJT.strftime("%Y %m %d %H").replace(" ","")
        timeList.append(timeBJTStr)
timeArray = np.array(timeList).T
#拼接其他数据
with open(stationFilePath,"r") as file1:
    list1 = file1.readlines()
    count = 0
    for i in range(len(list1)):
        stationId = list1[i].strip("\n")
        oneStationDataFile = oneStationDataFilePath + "new_"+stationId + ".txt"
        dataTemp = pd.read_csv(oneStationDataFile, sep=' ', engine = 'python', encoding="gbk" )
        count += 1
        dataTemp = np.array(dataTemp)
        print(stationId,dataTemp.shape)

'''
        timeArray = np.append(timeArray, dataTemp)
        #reshape(count, dataTemp.shape[0])
df2 = pd.DataFrame(timeArray.reshape(count-1, dataTemp.shape[0]))

print(df2)
'''