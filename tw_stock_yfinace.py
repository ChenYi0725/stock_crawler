from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tabulate import tabulate
import twstock
import yfinance as yf


# 使用 twstock 獲取資料
twstock_data = twstock.Stock("2330")
twstock_data = twstock.realtime.get("2330")
print("twstock:")
print(twstock_data)
# ====================
# 獲取 Apple 股票的數據
yf_data = yf.Ticker("2330.TW")
# 獲取 Apple 股票的歷史價格
# hist = yf_data.history(period="1mo")
hist = yf_data.history(period="1d")
print("yf_data:")
print(yf_data)
# 顯示數據
# print(hist)
