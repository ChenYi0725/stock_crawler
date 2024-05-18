from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tabulate import tabulate

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", value=True)
driver = webdriver.Chrome(options=chrome_option)


codes = ["1101.TW", "2330.TW", "2317.TW"]
data = []
titles = []
is_titles_acquired = False
for code in codes:
    driver.get(f"https://tw.stock.yahoo.com/quote/{code}")
    table = driver.find_element(
        By.XPATH, '//*[@id="qsp-overview-realtime-info"]/div[2]/div[2]/div/ul'
    )
    li_elements = table.find_elements(By.XPATH, "./li")
    data_row = []
    for li in li_elements:
        spans = li.find_elements(By.XPATH, "./span")
        data_row.append(spans[1].text)
        if not is_titles_acquired:
            titles.append(spans[0].text)
    data.append(data_row)
    is_titles_acquired = True
driver.quit()
df = pd.DataFrame(data, columns=titles)

print(df)


# titles = data[::2]
# contents = data[1::2]
