import hrbc
import sheet
import googleUtil

def main():
    
    dlQueList = googleUtil.readConfigSheet()
    hrbc.downloadCSV(dlQueList)
    sheet.uploadSpreadsheet(dlQueList)
    

if __name__ == '__main__':
    main()
