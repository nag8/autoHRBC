import csv
import util
import glob
import datetime
import os
import pandas as pd

import googleUtil





def uploadSpreadsheet():
    
    config = util.getConfig()
    dateStr = datetime.date.today().strftime("%Y-%m-%d")
    
    list = glob.glob(config['CSV']['DLPATH'] + '*.csv')
    list = [os.path.basename(r) for r in list]
    studentList = [[]]
    recruitList = [[]]
    
    for file in list:
        if '受講生フェーズ_' + dateStr in file:
            studentList.append(getList(config['CSV']['DLPATH'] + file))
            # print(lst)

            
        elif '受講生フェーズ（2019年）_' + dateStr in file:
            studentList.append(getList(config['CSV']['DLPATH'] + file))
            
        elif '選考プロセス_' + dateStr in file:
            recruitList.append(getList(config['CSV']['DLPATH'] + file))
            
    print(studentList)
    # googleUtil.uploadData(studentList)
    
def getList(csvPath):
    with open(csvPath, encoding="cp932") as f:
        reader = csv.reader(f)
        return [row for row in reader]
    
if __name__ == '__main__':
    uploadSpreadsheet()

