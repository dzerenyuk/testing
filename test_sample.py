from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestSample:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Firefox(executable_path=r'C:/DP/python/firefox/geckodriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
        wait = WebDriverWait(driver, 10)
        yield
        driver.close()
        driver.quit()

    def test_homa_page(self, test_setup):
        #driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
        #wait = WebDriverWait(driver, 10)
        assert 'Darwin Demosite' in driver.title

    def test_search_field(self, test_setup):
        #driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
        #wait = WebDriverWait(driver, 10)
        driver.find_element_by_id('search').send_keys('attorney', Keys.RETURN)
        #assert 'Filter By' in driver.page_source

    def test_menu_button(self, test_setup):
        driver.find_element_by_css_selector('#navigation > a').click()
        driver.find_element_by_css_selector(
            '#ctl00_ctl00_MainContentPlaceHolder_ctl00_ctl01_ulFirstList > li:nth-child(1) > a').click()
        assert 'Find' in driver.page_source
    def test_our_firm(self, test_setup):
        driver.find_element_by_css_selector(
            '#ctl00_ctl00_MainContentPlaceHolder_ctl01_ulFirstListFooter > li:nth-child(3) > a').click()
        assert 'Our Service Philosophy' in driver.page_source






