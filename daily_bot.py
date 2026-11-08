#System Imports
import time
from os import walk
import re
import socket
import random
import requests
import json
import shutil
import os
import logging          
import urllib
import urllib.request
from urllib.request import urlopen
import asyncio
from pathlib import Path
import subprocess
import tempfile
import base64
import io
import zipfile
import pickle
import websocket

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, WebDriverException
from auto_download_undetected_chromedriver import download_undetected_chromedriver

class daily_bot:   
    
    def start_driver(chromedriver_folder_path, headless=False):

        # Update ChromeDriver
        chromedriver_path = download_undetected_chromedriver(chromedriver_folder_path, undetected=True, arm=False, force_update=False)
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        # Dedicated persistent profile
        user_data_dir = r"C:\ChromeProfiles\Daily"
        os.makedirs(user_data_dir, exist_ok=True)

        options = uc.ChromeOptions()
        options.binary_location = chrome_path
        options.add_argument(f"--user-data-dir={user_data_dir}")

        if headless:
            options.add_argument("--headless=new")

        driver = uc.Chrome(options=options, driver_executable_path=chromedriver_path, browser_executable_path=chrome_path, version_main=156, use_subprocess=True)

        return driver

    def daily_rewards(chromedriver_folder_path, headless=False):

        try:
            os.system("taskkill /F /IM chrome.exe")
            os.system("taskkill /F /IM chromedriver.exe")
        except:
            pass
            
        #------------------#
        #   START DRIVER   #
        #------------------#
        driver = daily_bot.start_driver(chromedriver_folder_path, headless=False)
        
        #-----------------------#
        #   MICROSOFT REWARDS   #
        #-----------------------#
        
        website_to_login = "https://rewards.bing.com/dashboard?section=dailyset"
        o = 0
        while o == 0:
            try:
                driver.get(website_to_login)
                o = 1
            except TimeoutException as e:
                print("\n\n")
                print(f"[Timeout] {e}")
            except WebDriverException as e:
                print("\n\n")
                print(f"[Connection Error] {e.msg}")

        end = 0
        end1 = 0
        end2 = 0
        while end != 1 and end1 != 1 and end2 != 1:
            #Close Extra Tabs
            tab1 = driver.window_handles[0]
            while len(driver.window_handles) > 1:           
                tab2 = driver.window_handles[1]
                driver.switch_to.window(tab2)
                driver.close()
            driver.switch_to.window(tab1)

            try: #Daily Set 1
                driver.find_element(By.CSS_SELECTOR, "#react-aria-_R_4lav5t6bslbH2_ > div > div > a:nth-child(1)").click()
                print("\nMICROSOFT REWARDS: Daily Set 1 Clicked")
                time.sleep(2)
                end = 1
            except:
                pass
            try: #Daily Set 2
                driver.find_element(By.CSS_SELECTOR, "#react-aria-_R_4lav5t6bslbH2_ > div > div > a:nth-child(2)").click()
                print("\nMICROSOFT REWARDS: Daily Set 2 Clicked")
                time.sleep(2)
                end1 = 1
            except:
                pass
            try: #Daily Set 3
                driver.find_element(By.CSS_SELECTOR, "#react-aria-_R_4lav5t6bslbH2_ > div > div > a:nth-child(3)").click()
                print("\nMICROSOFT REWARDS: Daily Set 3 Clicked")
                time.sleep(2)
                end2 = 1
            except:
                pass
        
        driver.close()