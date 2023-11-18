from stock_data_web_scrapping import extract_data,transform,load_to_db

def main():
    extract_data()
    transform()
    load_to_db()
    
main()