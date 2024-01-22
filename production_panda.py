from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium
import requests
import logging
import os

class PandaSurveyAutomation:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        chrome_options = Options()
        options = [
            "--no-sandbox",
            "--headless",
            '--disable-gpu',
            '--disable-dev-shm-usage',
            "--window-size=1920,1080"
        ]
        for option in options:
            chrome_options.add_argument(option)

        chrome_options.add_argument('--remote-debugging-port=9222')
        self.driver = webdriver.Chrome(options=chrome_options)

    def quit_driver(self):
        if self.driver:
            self.driver.quit()

    def input_survey_code(self, code, last_digits):
        self.initialize_driver()
        
        try:
            self.driver.get("https://www.pandaguestexperience.com/")

            verify_length = code + last_digits
            length_no_spaces = verify_length.replace(" ", "")
            if len(length_no_spaces) != 22:
                raise Exception("Invalid code length")

            code_4_digit = code.split(" ")
            for i in range(1, 6):
                input_box = self.driver.find_element(By.NAME, "CN" + str(i))
                input_box.send_keys(code_4_digit[i - 1])
            input_box = self.driver.find_element(By.NAME, "CN6")
            input_box.send_keys(last_digits)

            link = self.driver.find_element(By.ID, "NextButton")
            link.click()

            next_link = self.driver.find_elements(By.ID, "NextButton")
            button_value = next_link[0].get_attribute('value')
            if button_value == "Start":
                raise Exception("Invalid code")

        except selenium.common.exceptions.NoSuchElementException:
            self.quit_driver()
            raise Exception("Wrong survey code")

    def fill_out_survey(self, email_addr):
        try:
            next_link = self.driver.find_elements(By.ID, "NextButton")
            while len(next_link) != 0:
                option_button = self.driver.find_elements(By.CLASS_NAME, "radioSimpleInput")
                email = self.driver.find_elements(By.NAME, "S000057")
                if len(email) != 0:
                    email = email[0]
                    email.send_keys(email_addr)
                    email = self.driver.find_element(By.NAME, "S000064")
                    email.send_keys(email_addr)
                    next_link = self.driver.find_elements(By.ID, "NextButton")
                    next_link[0].click()
                    break
                for i in range(0, len(option_button), 5):
                    option_button[i].click()
                next_link = self.driver.find_elements(By.ID, "NextButton")
                if len(next_link) == 0:
                    break
                next_link[0].click()

        except Exception as e:
            logging.exception("An error occurred:")
            # print(e)
        
        finally:
            # Call quit_driver after finishing the survey
            self.quit_driver()

    def increment_stat_count(self):
        try:
            api_url = 'https://api.api-ninjas.com/v1/counter?id=surveys_filled&hit=true'
            response = requests.get(api_url, headers={'X-Api-Key': os.environ.get("API_KEY")})
        except Exception as e:
            pass


def main():
    panda_survey_automation = PandaSurveyAutomation()
    
    try:
        code = input("Enter panda survey code (put space for '-'): ")
        email_addr = input("Enter email: ")
        last_digits = code[len(code) - 2:len(code):]
        code = code[:len(code) - 2:]
        
        panda_survey_automation.input_survey_code(code, last_digits)
        panda_survey_automation.fill_out_survey(email_addr)
        
    finally:
        panda_survey_automation.quit_driver()


if __name__ == "__main__":
    main()
