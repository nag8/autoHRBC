import csv
import util
import glob
import datetime
import os

import googleUtil





def uploadSpreadsheet():
    
    config = util.getConfig()
    dateStr = datetime.date.today().strftime("%Y-%m-%d")
    
    fList = glob.glob(config['CSV']['DLPATH'] + '*.csv')
    fList = [os.path.basename(r) for r in fList]
    studentList = []
    recruitList = []
    
    for file in fList:
        if '受講生フェーズ_' + dateStr in file:
            studentList = getList(config['CSV']['DLPATH'] + file)
            
        if '選考プロセス_' + dateStr in file:
            recruitList = getList(config['CSV']['DLPATH'] + file)
            
    for file in fList:
        if '受講生フェーズ（2019年）_' + dateStr in file:
            l = getList(config['CSV']['DLPATH'] + file)
            l.pop(0)
            studentList.extend(l)
    
    googleUtil.uploadData(studentList, 'work')
    googleUtil.uploadData(recruitList, 'work2')
    
def getList(csvPath):
    with open(csvPath, encoding="cp932") as fp:
        lst = list(csv.reader(fp))
    
    return lst
    
if __name__ == '__main__':
    uploadSpreadsheet()

