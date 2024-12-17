import time
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
service = Service("C:\\Users\\PC\\Downloads\\chromedriver.exe")

def get_driver():
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features = AutomationControlled")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def extract_number(text):
    """Extract only the temperature from the text"""
    output = text.split(":")
    return float(output[-1])


def main():
    driver = get_driver()
    driver.find_element(by= "id", value= "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by= "id", value= "id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(by= "xpath", value= "/html/body/nav/div/a").click()
    time.sleep(2)
    

print(main())