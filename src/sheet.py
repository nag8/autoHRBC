import csv
import util
import glob
import datetime
import os

import googleUtil





def uploadSpreadsheet():
    
    config = util.getConfig()

    studentList = []
    recruitList = []
    closeList = []
    logList = []

    dateStr = datetime.date.today().strftime("%Y-%m-%d")

    try:
        
        fList = glob.glob(config['CSV']['DLPATH'] + '*.csv')
        fList = [os.path.basename(r) for r in fList]
        
        for file in fList:
            if ('受講生フェーズ_' + dateStr) in file:
                studentList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('選考プロセス_' + dateStr) in file:
                recruitList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])

            if ('【関西】クローズ理由_' + dateStr) in file:
                closeList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])

            if ('企業管理データ(当月アプローチ企業)_' + dateStr) in file:
                approachList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('企業管理データ(契約締結)_' + dateStr) in file:
                policyList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('企業管理データ(リーガルチェック)_' + dateStr) in file:
                regalList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('企業管理データ(電話商談)_' + dateStr) in file:
                callList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('企業管理データ(オフライン商談)_' + dateStr) in file:
                offLineList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('企業管理データ(オンライン商談)_' + dateStr) in file:
                onLineList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
            if ('企業管理データ(アポ獲得)_' + dateStr) in file:
                appoList = getList(config['CSV']['DLPATH'] + file)
                logList.insert(0, ['upload成功_' + file])
                
        for file in fList:
            if ('受講生フェーズ（2019年）_' + dateStr) in file:
                l = getList(config['CSV']['DLPATH'] + file)
                l.pop(0)
                studentList.extend(l)
                logList.insert(0, ['upload成功_' + file])
        
        googleUtil.uploadData(studentList, config['GOOGLE']['SHEET_STUDENT'])
        googleUtil.uploadData(recruitList, config['GOOGLE']['SHEET_RECRUIT'])
        googleUtil.uploadData(closeList, config['GOOGLE']['SHEET_CLOSE'])
        googleUtil.uploadData(logList, config['GOOGLE']['SHEET_LOG'])
        googleUtil.uploadData(approachList, config['GOOGLE']['SHEET_APPROACH'])
        googleUtil.uploadData(policyList, config['GOOGLE']['SHEET_POLICY'])
        googleUtil.uploadData(regalList, config['GOOGLE']['SHEET_REGAL'])
        googleUtil.uploadData(callList, config['GOOGLE']['SHEET_CALL'])
        googleUtil.uploadData(offLineList, config['GOOGLE']['SHEET_OFFLINE'])
        googleUtil.uploadData(onLineList, config['GOOGLE']['SHEET_ONLINE'])
        googleUtil.uploadData(appoList, config['GOOGLE']['SHEET_APPO'])
    
    except Exception as e:
        logList = [['error! ' + dateStr]]
        googleUtil.uploadData(logList, config['GOOGLE']['SHEET_LOG'])
    
def getList(csvPath):
    with open(csvPath, encoding="cp932") as fp:
        lst = list(csv.reader(fp))
    
    return lst
    
if __name__ == '__main__':
    uploadSpreadsheet()

