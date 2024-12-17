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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def extract_number(text):
    """Extract only the temperature from the text"""
    output = text.split(":")
    return float(output[-1])

def create_text_file(text):
    """create a new text file with extract information"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%M-%H-%S')}.txt"
    with open(filename, "w") as scraped_file:
        scraped_file.write(text)

def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        dynamic_text = driver.find_element(by= "xpath", value= "/html/body/div[1]/div/h1[2]")
        output = str(extract_number(dynamic_text.text))
        create_text_file(output)

print(main())

