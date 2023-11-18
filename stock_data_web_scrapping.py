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

def transform():
    stock_data = pd.read_csv('data/ngx_stock_data.csv')  # Read csv file
    # Print existing column names
    print("Existing column names:", stock_data.columns)
    current_date = datetime.today().strftime("%Y-%m-%d")
    stock_data['date'] = current_date  # Change 'Date' to 'date'
    stock_data.columns = stock_data.columns.str.lower()
    # Re-arrange columns
    stock_data = stock_data[['date', 'ticker', 'name', 'volume', 'price', 'change']] 
    stock_data.to_csv('ngx_stock_data.csv', index=False)
    print('Data transformed and written to a csv file')


