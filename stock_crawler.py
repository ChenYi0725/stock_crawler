from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tabulate import tabulate
from PIL import Image
import requests
import yfinance as yf
from selenium.webdriver.chrome.service import Service
from PIL import Image
import io
import base64
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", value=True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(f"https://tw.stock.yahoo.com/quote/2330.TW")
table = driver.find_element(
    By.XPATH, '//*[@id="qsp-overview-realtime-info"]/div[2]/div[2]/div/ul'
)
li_elements = table.find_elements(By.XPATH, "./li")
for li in li_elements:
    spans = li.find_elements(By.XPATH, "./span")
    print(spans)
    # data = []
    # data_row.append(spans[1].text)
    # if not is_titles_acquired:
    #     titles.append(spans[0].text)

# data = []
# titles = []

#     for li in li_elements:
#         spans = li.find_elements(By.XPATH, "./span")
#         data = []
#         data_row.append(spans[1].text)
#         if not is_titles_acquired:
#             titles.append(spans[0].text)


# 關閉瀏覽器
driver.quit()

# 顯示股票走勢圖

# codes = ["1101.TW", "2330.TW", "2317.TW"]
# data = []
# titles = []
# is_titles_acquired = False
# for code in codes:
#     driver.get(f"https://tw.stock.yahoo.com/quote/{code}")
#     table = driver.find_element(
#         By.XPATH, '//*[@id="qsp-overview-realtime-info"]/div[2]/div[2]/div/ul'
#     )
#     li_elements = table.find_elements(By.XPATH, "./li")
#     data_row = []
#     for li in li_elements:
#         spans = li.find_elements(By.XPATH, "./span")
#         data_row.append(spans[1].text)
#         if not is_titles_acquired:
#             titles.append(spans[0].text)
#     data.append(data_row)
#     is_titles_acquired = True
# driver.quit()
# df = pd.DataFrame(data, columns=titles)
# df.index = codes
# print(df)
