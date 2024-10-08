# Instagram Followers
''' The code logins in to the user's Instagram account, locates followers of a given account, and automatically 
follows them. '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Setting up user-specific credentials and paths
CHROME_DRIVER_PATH = YOUR CHROM DRIVER PATH
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = YOUR INSTAGRAM USERNAME
PASSWORD = YOUR INSTAGRAM PASSWORD

# Class to handle Instagram following operations
class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    # Function to log in to Instagram
    def login(self):
        # Navigating to Instagram login page
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        # Finding username and password fields, entering credentials
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        # Submitting the login details
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    # Function to find followers of a specified account
    def find_followers(self):
        # Navigating to the account's followers list
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        # Scrolling through the followers list
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    # Function to follow the found followers
    def follow(self):
        # Locating and attempting to follow each follower
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # Handling exceptions due to element intercepting click
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

# Initializing the bot and executing actions
bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
