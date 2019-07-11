import time
import datetime
import requests
from urllib import request
from urllib.request import urlopen
import re

#获取雷达资料URL
def basrUrlStr(listTimeUTC,stationId):
    baseUrl1 = "http://10.181.89.55/cimiss-web/api?" \
              "userId=BEXN_QXT_6135537&" \
              "pwd=6135537&" \
              "interfaceId=getRadaFileByTimeRangeAndStaId&" \
              "dataCode=RADA_L2_UFMT&"
    baseUrl2 = "timeRange="+listTimeUTC+"&staIds="+stationId+"&dataFormat=text"
    baseUrl = baseUrl1 + baseUrl2
    return baseUrl
#获取时间列表
def timeFormat():
    nowStamp = time.time()
    nowStamp60sEarly = nowStamp - 600
    timeBeginUTC = int(datetime.datetime.utcfromtimestamp(nowStamp60sEarly).strftime("%Y%m%d%H%M%S"))
    timeEndUTC = int(datetime.datetime.utcfromtimestamp(nowStamp).strftime("%Y%m%d%H%M%S"))
    finalTimeListStr = "[" + str(timeBeginUTC) + "," + str(timeEndUTC) + "]"
    return finalTimeListStr
#存储目录
def downPath():
    with open("path.txt","r") as pathFile:
        path = pathFile.readlines()[0]
    return path
#下载雷达资料
def downloadRadarData(baseUrl,path):
    req = request.Request(baseUrl)
    response = urlopen(req).read().decode("utf-8")
    print(response)
    #path = "E:\\data\\"
    filename = "radartemp.txt"
    file1 = open(path + filename, "w")
    file1.write(response.strip("\n"))
    file1.close()
    with open(path + filename, "r") as file2:
        a = file2.readlines()
        for i in range(4, len(a)):
            singleRadarFileName = a[i].split(" ")[0]
            downloadUrl = a[i].split(" ")[3]
#            print(singleRadarFileName, downloatUrl)
            downloadFile = requests.get(downloadUrl)
            p1 = r"(RADA).*?(DOR).*?(Z\d.*)-.*?(C\w).*?(CAP).*?(\d.*)(.bin.bz2)"
            pattern1 = re.compile(p1)
            match1 = re.match(pattern1, singleRadarFileName)
            newName = "Z_RADR_I_" + match1.group(3) + "_" + match1.group(6) + "_O_" + match1.group(
                2) + "_" + match1.group(4) + "_" + match1.group(5) + match1.group(7)
            with open(path + match1.group(3)+"/"+newName, "wb") as code:
                code.write(downloadFile.content)
                print("Download finishied")
    return

if __name__ == "__main__":
    path = downPath()
    while True:
        timeRangeList = timeFormat()
        stationList = ["Z9970", "Z9971", "Z9974"]
        for stationId in stationList:
            baseUrl = basrUrlStr(timeRangeList,stationId)
            print(baseUrl)
            downloadRadarData(baseUrl,path)
        time.sleep(60)
    print("Done")



