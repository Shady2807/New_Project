from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com")
driver.find_element_by_id("tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element_by_xpath("id=flight-origin-hp-flight").send_keys(NYC)
driver1 = TouchActions()
driver1.double_tap("packageDirectFlight-hp-package")
time.sleep(2)
driver.find_element_by_id("search-button-hp-package").click()
driver.title()
driver.quit()










