import time
from selenium import webdriver
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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract only the temperature from the text."""
    output = text.split(":")
    return float(output[-1])

def main():
    driver = get_driver()
    time.sleep(5)
    element = driver.find_element(by= "xpath", value= "/html/body/div[1]/div/h1[2]")
    return clean_text(element.text) 

print(main())


