import csv
import util
import glob
import datetime
import os



def uploadSpreadsheet():
    
    config = util.getConfig()
    dateStr = datetime.date.today().strftime("%Y-%m-%d")
    
    list = glob.glob(config['CSV']['DLPATH'] + '/*.csv')
    list = [os.path.basename(r) for r in list]
    outList = []
    
    for file in list:
        if '受講生フェーズ（2019年）_' + dateStr in file:
            outList.append(file)
            
        elif '受講生フェーズ_' + dateStr in file:
            outList.append(file)
            
        elif '選考プロセス_' + dateStr in file:
            outList.append(file)
    
    print(outList)
    
    
if __name__ == '__main__':
    uploadSpreadsheet()

