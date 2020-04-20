from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import pandas as pd

def delay(n):
    time.sleep(randint(2, n))