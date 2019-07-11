import os

class CimissDataFirstLineDel(object):
    def __init__(self,dirPath,fileName):
        self.dirPath = dirPath
        self.fileName = fileName

    def firstLineDel(self):
        newFileName = "new_" + self.fileName
        oldFilePath = self.dirPath + self.fileName
        newFilePath = self.dirPath + newFileName
        with open(oldFilePath, "r") as oldFile:
            with open(newFilePath, "w") as newFile:
                for line in oldFile.readlines():
                    if "returnCode" not in line:
                        if "PRE" not in line:
                            newFile.write(line)
        os.remove(oldFilePath)


