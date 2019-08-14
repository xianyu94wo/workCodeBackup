from urllib import request
from urllib.request import urlopen

if __name__ == '__main__':
    # 1. 调用方法的参数定义，并赋值
    # 1.1 接口url
    # 1.2 用户名&密码
    # 1.3 接口ID
    # 1.4 必选参数（按需加可选参数）
    #     资料：中国地面逐小时
    #     检索要素：站号、站名、小时降水、气压、相对湿度、能见度、2分钟平均风速、2分钟风向
    #     检索时间
    #     排序：按照站号从小到大
    with open('E:/DATA/STATION_Number.txt',encoding='utf-8') as f1:
        list1 = f1.readlines()
        for i in list1:
            print(i.strip('\n'))
            baseUrl = 'http://10.181.89.55/cimiss-web/api?' \
                      'userId=BEXN_QXT_Yousangjie&' \
                      'pwd=Ysj8894315&' \
                      'interfaceId=getSurfEleByTimeRangeAndStaID&' \
                      'dataCode=SURF_CHN_MUL_HOR&' \
                      'elements=Year,Mon,Day,Hour,PRE_1h&' \
                      'timeRange=[20170101000000,20180101000000]&' \
                      'staIds='+i.strip('\n') +'&' \
                      'dataFormat=text'
        # 2. 调用接口

            req = request.Request(baseUrl)
            print(baseUrl)

            response = urlopen(req).read().decode("utf-8")
            # 3. 输出接口
            path = "E:/Rain1hForEveryNStation/NEW/"
            filename = i.strip('\n') + ".txt"
            file1 =  open(path+filename, "w")
            file1.write(response.strip("\n"))
            file1.close()
        print('Done!')

