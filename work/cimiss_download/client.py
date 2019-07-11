# Created on 2017/08/25
#
# @author: zhangxin
import datetime
from cma.cimiss.DataQueryClient import DataQuery

if __name__ == '__main__':
    # 定义client对象,指定数据服务ip和port
    # client = DataQuery(serverIp="10.181.89.55", serverPort=1888)
    # 定义client对象,通过默认使用client.config指定服务连接配置
    client = DataQuery()


    # 用户名和密码 需修改为自己的账号
    userName = "BEXN_QXT_ZNWG"
    password = "qxt6145537"

    # 接口ID
    interfaceId = "	getSurfEleInRegionByTime"

    # 当前时间减一天
    now_time = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime('%Y%m%d%H') + "0000"
    print('now_time:', now_time)

    # 接口参数
    params = {'dataCode': "SURF_CHN_MUL_HOR_N",
              'elements': "Station_ID_C,PRE_12h",
              'times': now_time,
              'adminCodes': "630100",
              'orderby': "Station_ID_C:ASC",
              'limitCnt': "100000"}

    retArray2D = ""

    # 调用接口
    # 1.获取数据返回结构体/类
    # retArray2D = client.callAPI_to_array2D(userName, password, interfaceId, params)

    # 2.获取数据返回序列化字符串
    # dataFormat 序列化的数据格式，可取：xml、json、csv、text、spaceText、commaText、tabText等。
    #            其中，spaceText、commaText、tabText表示保存为文本，记录间换行，要素值间分别用空格、逗号和TAB分割；text同spaceText。
    # retArray2D = client.callAPI_to_serializedStr(userName, password, interfaceId, params, dataFormat="csv")

    # 3.获取数据写入本地文件
    # dataFormat 序列化的数据格式，可取：xml、json、csv、text、spaceText、commaText、tabText等。
    #            其中，spaceText、commaText、tabText表示保存为文本，记录间换行，要素值间分别用空格、逗号和TAB分割；text同spaceText。
    # savePath 保持的本地文件路径（全路径，含文件名）

    # 保存文件的路径及文件名
    _saveDir_ = 'E:/test/data'
    # 一种字符串拼接方法
    _saveFile_ = '%s.txt' % now_time
    # 又一种字符串拼接方法
    _savePath_ = _saveDir_ + _saveFile_
    print('savePath:', _savePath_)

    result = client.callAPI_to_saveAsFile(userName, password, interfaceId, params, dataFormat='csv', savePath=_savePath_)
    # 输入结果预览
    print(retArray2D)

    # 销毁client对象
    client.destroy()

