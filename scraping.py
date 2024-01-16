import time
import re
import glob
import requests

from urllib.request import urlopen
from urllib import request

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')    # ヘッドレスモードに
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


URL = "https://tsukubadtm.bandcamp.com/"
driver.get(URL)
time.sleep(1)
element = driver.find_element_by_class_name('LinkBtn_More')
driver.execute_script("arguments[0].click();", element)

