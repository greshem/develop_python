from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#assert "Python" in driver.title
elem = driver.find_element_by_name("kw")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
#assert "Google" in driver.title
driver.close()
driver.quit()
