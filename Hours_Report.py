from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

import time
from datetime import date


URL = "https://mpg.co.il/login/?next=/"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
today = date.today()

# The date will always be the day the script is run
my_day = today.strftime("%d/%m/%Y")

# Change the hours according to your hours
start = "18:30"
end = "20:30"

# need to enter your id here
your_id = " "


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(URL)



username = driver.find_element(By.ID, "id_username")
username.send_keys(your_id)

password = driver.find_element(By.ID, "id_password")
password.send_keys(your_id)

submit = driver.find_element(By.CLASS_NAME, "btn")
submit.click()
time.sleep(3)


select = Select(driver.find_element(By.ID, "report_type"))
select.select_by_value("4")

set_day = driver.find_element(By.ID, "report_date")
set_day.send_keys(my_day)

set_time = driver.find_element(By.ID, "time_start")
set_time.send_keys(start)

end_time = driver.find_element(By.ID, "time_finish")
end_time.send_keys(end)

comments = driver.find_element(By.ID, "comments")
comments.send_keys("שיעור בפייתון לקבוצה שלי")

submit = driver.find_element(By.CLASS_NAME, "btn-info")
submit.click()

