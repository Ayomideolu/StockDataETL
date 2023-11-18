# StockDataETL
This project is about scrapping stock data of the Nigeria stock market to perform analysis and further prediction.

## Overview
On execution,this project pulls stock data from the Nigerian stock market website,data cleansing wasdone with the necessary dependencies,performs required transformation on the dataset,the data is hereby staged in the ngx_stock_data.csv in the vscode file explorer and also loads into a Postgresql database,for further analysis and decision making.

## Dependencies
This required libraries needed for running this code are in the requirement.txt

pandas
requests
sqlalchemy
python-dotenv
Setup
Setting up a postgresql database is required to run this code,create your database on psql.

## Database Credentials
In order to run the project, you need to set up your database credentials. Create a .env file in the project root directory and add the following information:

# Database Credentials
DB_USER_NAME = your_username
DB_PASSWORD = your_password
DB_NAME = your_database_name
PORT = your_database_port
HOST = your_database_host
Replace your_username, your_password, your_database_name, your_database_port, and your_database_host with your actual database credentials.

## Installation
Clone the repository:

git clone https://github.com/your-username/your-repository.git
Change into the project directory:

cd your-repository
Install the required dependencies:
pip install -r requirements.txt
Usage
stock_data_web_scrapping.py
This module handles the extraction, transformation, and loading of football data.
This module contain the extraction,transformation and loading of the football data gotten from the sport website.
util.py
This module contains helper functions to establish a database connection.

main.py
This is the main entry point for running the program.

python main.py