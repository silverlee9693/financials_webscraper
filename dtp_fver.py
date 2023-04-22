# install bs4, lxml, requests, pandas, selenium, webdriver_manager in CMD (admin)
# Create a folder named "Webscrape" on Desktop
# Rename the last line of code from 'zenbook' to your computer username


from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
from datetime import datetime
from selenium import webdriver
from csv import writer

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())) # DONOT CLOSE THE POP-UP CHROME WINDOWS

val = 'https://www.bursamalaysia.com/market_information/market_statistic/securities'
wait = WebDriverWait(driver, 10)
driver.get(val)

get_url = driver.current_url
wait.until(EC.url_to_be(val))

if get_url == val:
    page_source = driver.page_source

soup = BeautifulSoup(page_source,features='html.parser')

div_bs4 = soup.find('div', id = "daily_trading_participation")
markup = '''{0}'''.format(div_bs4)
dfs = pd.read_html(markup)


dtp = pd.DataFrame(dfs[1])

# Adjusting the timestamp and convert to strings
ts = pd.Timestamp.now()  
ts = ts.strftime('%d-%m-%Y %X')
str_ts = str(ts)

# Create a new column
time = [str_ts, str_ts, str_ts, str_ts]

# Add the column to our data
dtp['Time'] = time 

timestamp = datetime.now().strftime('%d-%m-%Y')
filename = f'dtp_{timestamp}.csv'

dtp.to_csv(f'C:/Users/zenbook/Desktop/Webscrape/{filename}', index=False)

