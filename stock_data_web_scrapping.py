import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from sqlalchemy import create_engine
from util import get_database_conn
con = get_database_conn

main_url = 'https://afx.kwayisi.org/ngx/'
list_of_df = []
# Data Extraction layer
def extract_data():
    for page in range(1, 3):
        url = main_url + f'?page={page}'  # Modify the URL for each page
        scrapped_data = requests.get(url)
        scrapped_data = scrapped_data.content
        soup = bs(scrapped_data, 'lxml')
        html_data = str(soup.find_all('table')[3])
        df = pd.read_html(html_data)[0]
        list_of_df.append(df)
    combined_data = pd.concat(list_of_df)
    combined_data.to_csv('data/ngx_stock_data.csv', index= False)
    print('Data Successfully written to a csv file')
