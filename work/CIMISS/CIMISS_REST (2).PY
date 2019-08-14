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

    baseUrl = "http://10.181.89.55/cimiss-web/api?" \
              "userId=BEXN_QXT_Yousangjie&pwd=Ysj8894315&" \
              "interfaceId=getSurfEleByTimeRangeAndStaID&dataCode=SURF_CHN_MUL_HOR&" \
              "elements=Year,Mon,Day,Hour&" \
              "timeRange=[20170101000000,20180101000000]&" \
              "staIds=52868&dataFormat=text"
    # 2. 调用接口

    req = request.Request(baseUrl)
    print(baseUrl)

    response = urlopen(req).read().decode("utf-8")
    print(response)
    # 3. 输出接口
    path = "E:/Rain1hForEveryNStation/"
    filename = "2017TIME.txt"
    file1 =  open(path+filename, "w")
    file1.write(response.strip("\n"))
    file1.close()
    print('Done!')

