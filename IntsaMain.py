from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from itertools import islice
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
class InstaBot():
    def __init__(self ):
        self.USERID = "shashank.6656"
        self.PASSWORD = "FGG0K18n!fPv!RI"
        self.targetUserid = ""
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
         
    def login(self, password, username):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        passwordres = self.driver.find_element(by=By.NAME, value="password")
        passwordres.send_keys(password)
        sleep(2)
        passwordres.send_keys(Keys.ENTER)
        save_login_info = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_info:
            save_login_info.click()
        turnon_notifications = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if turnon_notifications:
            turnon_notifications.click()
    def find_followers(self, targetid):
        self.driver.get(f"https://www.instagram.com/{targetid}/followers")
        sleep(2)
        xpath_of_follower_popup = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'
        follower_popup = self.driver.find_element(by=By.XPATH, value=xpath_of_follower_popup)
        for i in range(30):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)

    def startFollowing(self):
        list_of_followers = self.driver.find_elements(by=By.CSS_SELECTOR, value="._aano button")
        for button in list_of_followers:
            try:
                button.click()
                sleep(0.6)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
    def quitServer(self):
        self.driver.quit()



