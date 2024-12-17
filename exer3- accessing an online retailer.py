import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
service = Service("C:\\Users\\PC\\Downloads\\chromedriver.exe")

def get_driver():
    """set options to make browsing easier"""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features = AutomationControlled")
    driver = webdriver.Chrome(service= service, options= options)
    driver.get("https://finance.yahoo.com/quote/AAPL/history/?period1=345479400&period2=1717271822")
    time.sleep(2)
    return driver

def main():
    driver= get_driver()
    time.sleep(5)
    
    


print(main())