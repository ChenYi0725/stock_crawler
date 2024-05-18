from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tabulate import tabulate

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", value=True)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://tw.stock.yahoo.com/quote/1101.TW")


table = driver.find_element(
    By.XPATH, '//*[@id="qsp-overview-realtime-info"]/div[2]/div[2]/div/ul'
)
li_elements = table.find_elements(By.XPATH, "./li")

print(li_elements)
data = []
for element in li_elements:
    data.append(element.text)
for item in data:
    print(item)
driver.quit()
