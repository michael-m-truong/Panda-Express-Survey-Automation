from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options

def inputSurveyCode(code, lastDigits):
    global driver
    # chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    chrome_options = Options()
    options = [
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver.exe", options=chrome_options)
    driver.get("https://www.pandaguestexperience.com/")

    verifyLength = code + lastDigits
    lengthNoSpaces= verifyLength.replace(" ", "")
    if len(lengthNoSpaces) != 22:
        driver.quit()
        raise Exception("Invalid code length")

    code4Digit = code.split(" ")
    for i in range(1,6):
        inputBox = driver.find_element(By.NAME, "CN"+str(i))
        print(code4Digit[i-1])
        inputBox.send_keys(code4Digit[i-1])
    inputbox = driver.find_element(By.NAME, "CN6")
    inputbox.send_keys(lastDigits)

    try:
        link = driver.find_element(By.ID, "NextButton")
        link.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("Wrong survey code")
        driver.quit()
    nextLink = driver.find_elements(By.ID, "NextButton")
    buttonValue =  nextLink[0].get_attribute('value')
    if buttonValue == "Start":
        driver.quit()
        raise Exception("Invalid code")


def FillOutSurvey(email_addr):
    nextLink = driver.find_elements(By.ID, "NextButton")
    while len(nextLink) != 0:
        optionButton = driver.find_elements(By.CLASS_NAME, "radioSimpleInput")
        email = driver.find_elements(By.NAME, "S000057")
        if len(email) != 0:
            email = email[0]
            email.send_keys(email_addr)
            email = driver.find_element(By.NAME, "S000064")
            email.send_keys(email_addr)
            nextLink = driver.find_elements(By.ID, "NextButton")
            nextLink[0].click()
            break
        for i in range(0, len(optionButton), 5):
            optionButton[i].click()
        nextLink = driver.find_elements(By.ID, "NextButton")
        if len(nextLink) == 0:
            break
        nextLink[0].click()

def main():
    code = input("Enter panda survey code (put space for '-'): ")
    email_addr = input("Enter email: ")
    lastDigits = code[len(code)-2:len(code):]
    code = code[:len(code)-2:]
    inputSurveyCode(code, lastDigits)
    FillOutSurvey(email_addr)
  
    
if __name__ == "__main__":
    main()