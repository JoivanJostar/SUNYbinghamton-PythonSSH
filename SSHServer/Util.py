import argparse
import os


class utility:
    def __init__(self):
        print("create util object")


    def str_readPWD(self, datasPerLine):
        if datasPerLine <= 0:
            raise Exception("Invalid dataPerLine!", datasPerLine)
        str_files = ""
        cnt = 0
        file_lists = os.listdir("./")
        for file in file_lists:
            if (cnt < datasPerLine - 1):
                seperator = "\t"
            else:
                seperator = "\n"
            str_files += (file + seperator)
            cnt += 1
            if (cnt == datasPerLine):
                cnt = 0
        return str_files

    def getPWD(self):
        return os.getcwd()
