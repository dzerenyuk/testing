from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path=r'C:\\DP\\python\\chrome\\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\\DP\\python\\firefox\\geckodriver.exe')
print(type(webdriver.Firefox))
#driver.maximize_window()

#driver.get('http://lollilatte:hotEdge21@darwindemosite.staging.tenrec.com')
#driver.find_element_by_id('search').send_keys('attorney', Keys.RETURN)
#wait = WebDriverWait(driver, 10)
#driver.back()



#assert 'Our Service Philosophy' in driver.page_source











