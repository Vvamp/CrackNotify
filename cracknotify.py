import os
from twilio.rest import Client
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options 
import time 
import logging
logging.basicConfig(filename="cracknotify.log")
logging.info('Init')
status = "UNCRACKED"
while status != "CRACKED":
    logging.info('Loading webpage')
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    # driver.implicitly_wait(15)
    driver.get('https://crackwatch.com/game/assassin-s-creed-valhalla') # driver.find_element_by_class_name('status-bottom')
    time.sleep(5)
    statusblock = driver.find_element_by_class_name('status-bottom')
    status = statusblock.text
    driver.close()
    if status != "CRACKED":
        logging.info('Waiting for next load...')
        time.sleep(60)

if status == "CRACKED":
    logging.info("AC:V Has been cracked!")
    account_sid = os.environ['SIDTKN']
    auth_token = os.environ['AUTHTKN']
    # account_sid = 'AC887fab7cb6dc1f73e76e3e16951e2349'
    # auth_token = 'b8ec3bf4269732dbd00f6614371ad057'
    client = Client(account_sid, auth_token)
    logging.info("Sending Messages...")
    recips = ['+31640716369', '31644945378']
    for recip in recips:
        message = client.messages \
            .create(
                body='AC:V Has been cracked!',
                from_='+18038794475',
                to=recip
            )

        print(message.sid)
        print(message)
    logging.info("Messages have been sent!")
    print("Game has been cracked!")