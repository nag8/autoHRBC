import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

import util
import dlQue

def readConfigSheet():
    
    config = util.getConfig()
    gc = prepare(config)

    wks = gc.open_by_key(config['GOOGLE']['SPREADSHEET']).worksheet(config['GOOGLE']['SHEET_CONFIG'])
    cell_list = wks.get_all_values()
    cell_list.pop(0)
    
    outList = []
    for row in cell_list:
        outList.append(dlQue.DlQue(row[0], row[1], row[2]))
        
    print(outList)
    return outList

def uploadData(data, sheetName):
    
    config = util.getConfig()
    gc = prepare(config)

    wks = gc.open_by_key(config['GOOGLE']['SPREADSHEET']).worksheet(sheetName)
    wks.clear()
    wks.update('A1', data)


def prepare(config):
    #2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    #認証情報設定
    credentials = ServiceAccountCredentials.from_json_keyfile_name(config['GOOGLE']['JSON'], scope)
    return gspread.authorize(credentials)

if __name__ == '__main__':
    # uploadData([[1, 2], [3, 4]], 'work')
    readConfigSheet()
