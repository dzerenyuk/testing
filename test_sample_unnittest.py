'''from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:/DP/python/firefox/geckodriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_homa_page(self):
        self.driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
        wait = WebDriverWait(self.driver, 10)
        assert 'Darwin Demosite' in self.driver.title

    def test_search_field(self, test_setup):
        self.driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_id('search').send_keys('attorney')
        element = self.driver.find_element_by_id('search')
        element.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    service = TestClass()
    service.tearDown()
    unittest.main()
'''






