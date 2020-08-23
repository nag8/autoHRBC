import csv
import util
import glob
import datetime
import os

import googleUtil


def uploadSpreadsheet(dlQueList):
    
    config = util.getConfig()
    dateStr = datetime.date.today().strftime("%Y-%m-%d")
    logList = []

    try:
        
        fList = glob.glob(config['CSV']['DLPATH'] + '*.csv')
        fList = [os.path.basename(r) for r in fList]
        
        for dlQue in dlQueList:
            googleUtil.clear(dlQue.sheetName)
        
        
        for dlQue in dlQueList:
            for file in fList:
                if (dlQue.fileName + dateStr) in file:
                    list = getList(config['CSV']['DLPATH'] + file)
                    
                    if dlQue.addFlg == "TRUE":
                        list.pop(0)
                    
                    googleUtil.uploadData(list, dlQue.sheetName)
                    logList.insert(0, ['upload成功_' + file])
    
        googleUtil.uploadData(logList, config['GOOGLE']['SHEET_LOG'])

    except Exception as e:
        print(e)
        logList = [['error! ' + dateStr]]
        googleUtil.uploadData(logList, config['GOOGLE']['SHEET_LOG'])
    
def getList(csvPath):
    with open(csvPath, encoding="cp932") as fp:
        lst = list(csv.reader(fp))
    
    return lst
    
if __name__ == '__main__':
    uploadSpreadsheet()

