from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time


URL = "https://mpg.co.il/login/?next=/"
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(URL)


username = driver.find_element(By.ID, "id_username")
username.send_keys("my_id")

password = driver.find_element(By.ID, "id_password")
password.send_keys("my_id")

submit = driver.find_element(By.CLASS_NAME, "btn")
submit.click()
time.sleep(3)

report_type = driver.find_element(By.ID, "report_type")
report_type.click()

select = Select(report_type)
select.select_by_value("4")

time.sleep(1)

# TODO understent why it not working!

report_date = driver.find_element(By.ID, "report_date")
ActionChains(report_date).click()
time.sleep(5)

# report_date.click()

time_start = driver.find_element(By.ID, "time_start")

time_finish = driver.find_element(By.ID, "time_finish")



