from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from string import digits
from datetime import date
import time, os
from itertools import cycle

user_path = "."
executable = ".\\geckodriver\\geckodriver.exe"

#Account details
username = ""
password = ""

#Login status, don´t change it
login = 0

options = Options()
#Delete the # at the start of the line below to enable headless browser
#options.add_argument("--headless") 

driver = webdriver.Firefox(options=options, executable_path=executable) 

with open(".\\text.txt") as tags_final:
    tags_final = tags_final.readlines()
tags_final = tags_final[0:4]
kw1, kw2, tags, description = tags_final[0], tags_final[1], tags_final[2], tags_final[3]

while login == 0:
    driver.get("https://stackoverflow.com/users/signup")
    stack_google = driver.find_element_by_css_selector("button.grid--cell.s-btn.s-btn__icon.s-btn__google.bar-md.ba.bc-black-100").click()
    print("Login through stack")
    time.sleep(3)
    actions = ActionChains(driver)
    actions.send_keys(username)
    actions.perform()
    print(f"Login with email")
    actions2 = ActionChains(driver)
    actions2.send_keys(Keys.ENTER)
    actions2.perform()
    time.sleep(3)
    actionspsw = ActionChains(driver)
    actionspsw.send_keys(password)
    actionspsw.perform()
    print(f"Login with password")
    actions2.perform()
    time.sleep(5)
    print("Succesful login")
    login += 1
    if login > 0:
        for i in cycle(range(0,1)):
            for x in os.listdir(user_path):
                try:
                    if x.endswith(".mp4"):
                        driver.get("https://youtube.com/upload")
                        time.sleep(10)
                        videos = (os.path.abspath(x))
                        upload = driver.find_element_by_xpath("//input[@type='file']").send_keys(videos)
                        print(f"Uploading the video {x}")
                        time.sleep(10)
                        title_text = Path(videos).stem
                        title_text_translate = str.maketrans("_", " ", digits)
                        title_text = title_text.translate(title_text_translate) + kw1 + " " + kw2 + " " + date.today().strftime("%d %B, %Y")
                        textfinder = driver.find_elements_by_id("textbox")
                        title = (textfinder[0]).send_keys(title_text)
                        time.sleep(5)
                        desc = (textfinder[1]).send_keys(description)
                        children = driver.find_elements_by_id("radioContainer")
                        children = (children[1]).click()
                        advanced_options = driver.find_element_by_css_selector("ytcp-button.advanced-button.style-scope.ytcp-uploads-details").click()
                        tagsselect = ActionChains(driver)
                        tagsselect = driver.find_elements_by_class_name("text-input.style-scope.ytcp-chip-bar")
                        tagsselect = (tagsselect[1]).send_keys(tags)
                        nextbutton = driver.find_element_by_id("next-button").click()
                        time.sleep(3) 
                        secondbutton = driver.find_element_by_id("next-button").click()
                        time.sleep(3)
                        video_settings = driver.find_elements_by_id("radioContainer")
                        video_settingspublic = (video_settings[3]).click()
                        donebutton = driver.find_element_by_id("done-button").click()
                        os.remove(x)
                        time.sleep(10)
                except:
                    print("There are no video files it will be tried again in 30 seconds.")
                    continue




