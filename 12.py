from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path=r'C:\\DP\\python\\chrome\\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\\DP\\python\\firefox\\geckodriver.exe')
driver.maximize_window()
driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
driver.find_element_by_css_selector(
    '#ctl00_ctl00_MainContentPlaceHolder_ctl01_ulFirstListFooter > li:nth-child(3) > a').click()
assert 'Our Service Philosophy' in driver.page_source











