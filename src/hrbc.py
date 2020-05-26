from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import util
import logging
import traceback

def getCSV():
    
    config = util.getConfig()
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://hrbc-jp.porterscloud.com/common/navigation')

        # ログイン画面
        driver.find_element_by_id('Model_LoginForm_company_login_id').send_keys(config['HRBC']['COMPANY'])
        driver.find_element_by_id('Model_LoginForm_username').send_keys(config['HRBC']['ID'])
        driver.find_element_by_id('Model_LoginForm_password').send_keys(config['HRBC']['PASS'])
        driver.find_element_by_id('login-form').submit()
        
        driver.find_element_by_class_name('ui-button-text-only').click()
        
        time.sleep(5)
        
        # レポートダウンロード
        driver.get(config['HRBC']['CSV_1'])
        driver.get(config['HRBC']['CSV_2'])
        driver.get(config['HRBC']['CSV_3'])
        
        time.sleep(10)

        
    except Exception as e:
        logging.error(traceback.format_exc())

    finally:
        driver.quit()
