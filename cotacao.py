from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
# assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("cotaçao dolar")
# sleep(5)
elem.send_keys(Keys.RETURN)

valor_real = driver.find_element(By.CLASS_NAME, 'b1hJbf')
assert "No results found." not in driver.page_source
print(valor_real.text)
driver.close()