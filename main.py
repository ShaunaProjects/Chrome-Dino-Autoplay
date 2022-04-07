import PIL
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

chrome_drive_path = os.environ.get("drive_path")
ser = Service(chrome_drive_path)
driver = webdriver.Chrome(service=ser)
url = "https://chromedino.com/"
driver.get(url)
actions = ActionChains(driver)

def check_obstacle():
    obstacle_rgb = (83, 83, 83)
    img = pyautogui.screenshot()
    y = 363
    for x in range(290, 315):
        if img.getpixel((x, y)) == obstacle_rgb:
            jump()

def jump():
    actions.send_keys(Keys.SPACE)
    actions.perform()

def play_game():
    time.sleep(2)
    actions.send_keys(Keys.SPACE)
    actions.perform()
    game_running = True
    while game_running:
        check_obstacle()

play_game()