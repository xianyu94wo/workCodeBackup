#!/usr/bin/env python
# coding=utf8

import DataBlock_pb2
import GDS_data_service
import struct


def configData():
    with open("config2.ini","r",encoding='utf-8') as file1:
        config = file1.readlines()
    return config



#数据目录
#directory = "GRAPES_MESO_HR/RH/500"
#output_directory = "E:/Data/moshi/GRAPES_MESO/RH/500/"
listTemp = configData()
print(len(listTemp))
x = len(listTemp)
a = listTemp.index('分布式路径：\n')
b = listTemp.index('存储路径：\n')
c = listTemp.index('时间步长：\n')
list1 = []
list2 = []
list3 = []
for i in range(a+1, b):
    list1.append(listTemp[i].strip('\n'))
for i in range(b+1, c):
    list2.append(listTemp[i].strip('\n'))
for i in range(c+1,x):
    list3.append(listTemp[i].strip('\n'))
print(list1)
print(list2)
print(list3)
periods = int(list3[0])

for i in range(len(list1)):
    directory = list1[i]
    output_directory = list2[i]
    #初始化GDS客户端
    service = GDS_data_service.GDSDataService("10.181.22.103", 8080)
    #获得指定目录下的所有文件
    status ,response = service.getFileList(directory)
    MappingResult = DataBlock_pb2.MapResult()
    #如果返回状态为200(Success)
    if status == 200:
        if MappingResult is not None:
            #Protobuf的解析
            MappingResult.ParseFromString(response)
            results = MappingResult.resultMap
            #遍历指定目录
            for name_size_pair in results.items():
                #文件名
                fileName = name_size_pair[0]
                #http请求
                status, response = byteArrayResult = service.getData(directory, fileName)
                ByteArrayResult = DataBlock_pb2.ByteArrayResult()
                if status == 200:
                    ByteArrayResult.ParseFromString(response)
                    if ByteArrayResult is not None:
                        try:
                            byteArray = ByteArrayResult.byteArray
                            #print(len(byteArray))
                            discriminator =struct.unpack("4s",byteArray[:4])[0].decode("gb2312")
                            t = struct.unpack("h",byteArray[4:6])
                            mName = struct.unpack("20s",byteArray[6:26])[0].decode("gb2312")
                            eleName = struct.unpack("50s",byteArray[26:76])[0].decode("gb2312")
                            description = struct.unpack("30s",byteArray[76:106])[0].decode("gb2312")
                            level,y,m,d,h,timezone,period = struct.unpack("fiiiiii",byteArray[106:134])
                            startLon,endLon,lonInterval,lonGridCount = struct.unpack("fffi",byteArray[134:150])
                            startLat,endLat,latInterval,latGridCount = struct.unpack("fffi",byteArray[150:166])
                            isolineStartValue,isolineEndValue,isolineInterval =struct.unpack("fff",byteArray[166:178])
                            gridCount = lonGridCount*latGridCount
                            description =mName.rstrip('\x00')+'_'+eleName.rstrip('\x00')+"_"+str(level)+'('+description.rstrip('\x00')+')'+":"+str(period)
                            print(level, y, m, d, h, timezone, period)
                            if (gridCount == (len(byteArray)-278)/4) and period < periods:
                                #保存MICAPS4类数据
                                print("下载",level, y, m, d, h, timezone, period)
                                print(directory)
                                with open (output_directory+fileName,'w') as writer:
                                    eachline = "diamond 4 "+description
                                    writer.write(eachline+"\n")
                                    eachline = str(y)+"\t"+str(m)+"\t"+str(d)+"\t"+str(h)+"\t"+str(period)+"\t"+str(level)+"\t"\
                                    +str(lonInterval)+"\t"+str(latInterval)+"\t"+str(round(startLon,2))+"\t"\
                                    +str(endLon)+"\t"+str(round(startLat,2))+"\t"+str(round(endLat,2))+\
                                    "\t"+str(lonGridCount)+"\t"+str(latGridCount)+"\t"+\
                                    str(isolineInterval)+"\t"+str(isolineStartValue)+"\t"+\
                                    str(isolineEndValue)+"    3    0"
                                    writer.write(eachline+"\n")
                                    for i in range(gridCount):
                                        if (i != 0 and i % 10 == 0):
                                            writer.write('\n')
                                        gridValue = struct.unpack("f",byteArray[278+i*4:282+i*4])[0]
                                        writer.write(str(round(gridValue,2)).ljust(10))
                        except:
                            print('not ok')

print("Done!")

# #!/usr/bin/env python
# # coding=utf8
#
# import DataBlock_pb2
# import GDS_data_service
# import struct
#
#
# def configData():
#     with open("config.ini","r") as file1:
#         config = file1.readlines()
#     return config
#
#
#
# #数据目录
# #directory = "GRAPES_MESO_HR/RH/500"
# #output_directory = "E:/Data/moshi/GRAPES_MESO/RH/500/"
# directory = configData()[0].strip("\n")
# output_directory = configData()[1].strip("\n")
# periods = int(configData()[2])
# #初始化GDS客户端
# service = GDS_data_service.GDSDataService("10.181.22.103", 8080)
# #获得指定目录下的所有文件
# status ,response = service.getFileList(directory)
# MappingResult = DataBlock_pb2.MapResult()
# #如果返回状态为200(Success)
# if status == 200:
#     if MappingResult is not None:
#         #Protobuf的解析
#         MappingResult.ParseFromString(response)
#         results = MappingResult.resultMap
#         #遍历指定目录
#         for name_size_pair in results.items():
#             #文件名
#             fileName = name_size_pair[0]
#             #http请求
#             status, response = byteArrayResult = service.getData(directory, fileName)
#             ByteArrayResult = DataBlock_pb2.ByteArrayResult()
#             if status == 200:
#                 ByteArrayResult.ParseFromString(response)
#                 if ByteArrayResult is not None:
#                     byteArray = ByteArrayResult.byteArray
#                     #print(len(byteArray))
#                     discriminator =struct.unpack("4s",byteArray[:4])[0].decode("gb2312")
#                     t = struct.unpack("h",byteArray[4:6])
#                     mName = struct.unpack("20s",byteArray[6:26])[0].decode("gb2312")
#                     eleName = struct.unpack("50s",byteArray[26:76])[0].decode("gb2312")
#                     description = struct.unpack("30s",byteArray[76:106])[0].decode("gb2312")
#                     level,y,m,d,h,timezone,period = struct.unpack("fiiiiii",byteArray[106:134])
#                     startLon,endLon,lonInterval,lonGridCount = struct.unpack("fffi",byteArray[134:150])
#                     startLat,endLat,latInterval,latGridCount = struct.unpack("fffi",byteArray[150:166])
#                     isolineStartValue,isolineEndValue,isolineInterval =struct.unpack("fff",byteArray[166:178])
#                     gridCount = lonGridCount*latGridCount
#                     description =mName.rstrip('\x00')+'_'+eleName.rstrip('\x00')+"_"+str(level)+'('+description.rstrip('\x00')+')'+":"+str(period)
#                     print(level, y, m, d, h, timezone, period)
#                     if (gridCount == (len(byteArray)-278)/4) and period < periods:
#                         #保存MICAPS4类数据
#                         print("下载",level, y, m, d, h, timezone, period)
#                         with open (output_directory+fileName,'w') as writer:
#                             eachline = "diamond 4 "+description
#                             writer.write(eachline+"\n")
#                             eachline = str(y)+"\t"+str(m)+"\t"+str(d)+"\t"+str(h)+"\t"+str(period)+"\t"+str(level)+"\t"\
#                             +str(lonInterval)+"\t"+str(latInterval)+"\t"+str(round(startLon,2))+"\t"\
#                             +str(endLon)+"\t"+str(round(startLat,2))+"\t"+str(round(endLat,2))+\
#                             "\t"+str(lonGridCount)+"\t"+str(latGridCount)+"\t"+\
#                             str(isolineInterval)+"\t"+str(isolineStartValue)+"\t"+\
#                             str(isolineEndValue)+"    3    0"
#                             writer.write(eachline+"\n")
#                             for i in range(gridCount):
#                                 if (i != 0 and i % 10 == 0):
#                                     writer.write('\n')
#                                 gridValue = struct.unpack("f",byteArray[278+i*4:282+i*4])[0]
#                                 writer.write(str(round(gridValue,2)).ljust(10))
#
# print("Done!")
#
#
# GRAPES_MESO_HR/RH/500
# E:/Data/moshi/GRAPES_MESO/RH/500/
# 84