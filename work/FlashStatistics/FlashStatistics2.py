import os
import pandas as pd

def dataFrameProcess(filePath):
    #读取资料
    dfTemp = pd.read_table(filePath, encoding='gb2312', sep=',', engine='python')
    #合并日期和时间列
    dfTime = dfTemp['日期'].str.cat(dfTemp['时间'],sep=' ')
    #转合并后的列为pandas时间
    dfTime = pd.to_datetime(dfTime)
    #将结果插入第三列后
    dfTemp.insert(3,'日期&时间',dfTime)
    #删除原来的日期和时间列
    dfTemp.drop(['日期','时间'],axis=1,inplace=True)
    #按日期和时间排序
    dfTemp.sort_values('日期&时间',inplace=True)
    #删除第一列
    dfTemp.drop(dfTemp.columns[0],axis=1,inplace=True)
    #整理好的dataframe写入temp
    dfTemp.to_csv('E:/dfTempA.txt')

def thunderProcess1(nameOfCounty):
    #读取新dataframe
    dfTemp2 = pd.read_table('E:/dfTempA.txt', encoding='utf-8', sep=',', engine='python')
    dfTemp2.drop(dfTemp2.columns[0],axis=1,inplace=True)
    #转换日期时间列为pddatetime格式
    dfTime2 = pd.to_datetime(dfTemp2['日期&时间'])
    #插入转好的列
    dfTemp2.insert(1,'时间&日期',dfTime2)
    #删除原有列
    dfTemp2.drop(['日期&时间'],axis=1,inplace=True)
    #错行相减
    dfTemp3 = dfTemp2['时间&日期'] - dfTemp2['时间&日期'].shift(1)
    #设置时间差
    timeDelta = pd.Timedelta('1 hour')
    #计算前后时间
    listDrop = []
    listAll = []
    #求出时间差超过一小时的行并放入listdrop中
    for index,timestamp in enumerate(dfTemp3):
        if timestamp > timeDelta :
            listDrop.append(index - 1)
    for i in range(len(dfTemp2)):
        listAll.append(i)
    listFinal = list(set(listAll)^set(listDrop))
    dfTempDrop = dfTemp2.drop(index=listDrop)
    listTemp1 = [2]
    listTemp2 = []
    #求相隔两次闪电间的标签差值
    for i in range(len(listFinal)-1):
        a = listFinal[i+1]-listFinal[i]
        listTemp1.append(a)
    #如果标签差不等于1，表示不连续，即为两次过程
    for i in range(len(listTemp1)):
        if listTemp1[i] != 1:
            listTemp1[i] = 0
            listTemp2.append(i)
    #将不连续的时间点在listTemp1中的位置输出至列表中
    listTemp2.append(len(listFinal))
    #输出两次不连续时间点之间的位置至listTemp3中
    #选取大于5次的过程
    for i in range(len(listTemp2)-1):
        listTemp3 = listFinal[listTemp2[i]:listTemp2[i + 1]]
        if len(listTemp3) > 4:
            dfThunderStart = dfTempDrop.loc[[listTemp3[0]]]
            dfThunderEnd = dfTempDrop.loc[[listTemp3[-1]]]
            dfThunderFinal = pd.concat([dfThunderStart,dfThunderEnd])
            dfThunderFinal.to_csv('E:/dfTempB.TXT', sep=",", index=False)
            with open('E:/dfTempB.txt', 'r', encoding='utf-8') as f1:
                listThunderStart = f1.readlines()
                strThunderStart = '雷暴开始：' + listThunderStart[1]
                strThunderEnd = '雷暴结束：' + listThunderStart[2]
                strThunderFrequency = '雷暴次数：' + str(len(listTemp3)+1) + '\n'
            fileTempName = 'E:/' +  nameOfCounty + '雷暴统计.txt'
            with open(fileTempName,'a', encoding='utf-8') as f2:
                f2.write(strThunderStart)
                f2.write(strThunderEnd)
                f2.write(strThunderFrequency)


if __name__ == '__main__':
    resultPath = 'E:/FlashStatistics各县逐年/'
    listFile = os.listdir(resultPath)
    for eachFile in listFile:
        filePath = resultPath + eachFile
        nameOfCounty = eachFile[:-4]
        dataFrameProcess(filePath)
        thunderProcess1(nameOfCounty)

    print('ALL DONE!')




