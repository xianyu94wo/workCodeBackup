from urllib import request
from urllib.request import urlopen
class downloadDataFromCimiss(object):
    def __init__(self):
        self.filename = input(str("请输入文件储存名（需带有后缀）"))
        self.path = input(str("请输入文件储存目录（使用斜杠）")) + "\\"
        self.baseUrl = input(str("请输入URL"))
    def requestToCimiss(self):
        req = request.Request(self.baseUrl)
        response = urlopen(req).read().decode("utf-8")
        file1 = open(self.path + self.filename, "w")
        file1.write(response.strip("\n"))
        file1.close()

    #baseUrl = "http://10.181.89.55/cimiss-web/api?userId=BEXN_QXT_Yousangjie&pwd=Ysj8894315&interfaceId=getSurfEleInRegionByTimeRange&dataCode=SURF_CHN_MUL_HOR&timeRange=[20180901000000,20181001010000]&adminCodes=630000&elements=Station_Id_C,Year,Mon,Day,Hour,PRE_1h&eleValueRanges=PRE_1h:[10,999)&dataFormat=text"
if __name__ == '__main__':
    down = downloadDataFromCimiss()
    down.requestToCimiss()
    print('Done!')
