from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import util
import googleUtil
import logging
import traceback

def downloadCSV(dlQueList):
    
    config = util.getConfig()
    
    
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options,executable_path=config['CHROME']['PATH'])

    try:
        driver.get('https://hrbc-jp.porterscloud.com/common/navigation')

        # ログイン画面
        driver.find_element_by_id('Model_LoginForm_company_login_id').send_keys(config['HRBC']['COMPANY'])
        driver.find_element_by_id('Model_LoginForm_username').send_keys(config['HRBC']['ID'])
        driver.find_element_by_id('Model_LoginForm_password').send_keys(config['HRBC']['PASS'])
        driver.find_element_by_id('login-form').submit()
        
        if len(driver.find_elements_by_class_name('ui-button-text-only')) > 0:
            driver.find_element_by_class_name('ui-button-text-only').click()
        
        time.sleep(5)
        
        for dlQue in dlQueList:
            download(driver, dlQue.url)
        
    except Exception as e:
        logging.error(traceback.format_exc())

    finally:
        driver.quit()

# レポートダウンロード
def download(driver,url):
    driver.get(url)
    time.sleep(20)
    driver.find_element_by_class_name('download').click()
    time.sleep(10)
