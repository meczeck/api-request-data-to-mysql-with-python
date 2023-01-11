import requests
import db_connect
import config_read

api_key = config_read.config_file['api_key']
response = requests.get("https://v6.exchangerate-api.com/v6/%s/latest/TZS"%api_key)

#List to store target currencies
target_currencies = ['USD', 'GBP', 'KES', 'EUR']


# cursor object c
c = db_connect.db_connection.cursor()

for i in target_currencies:
    rate = response.json()['conversion_rates'][i]
    
    insert_query = "INSERT INTO exchange_rates(target_currency, conversion_rate) VALUES (%s,%s)"
    data = (i, rate)
    c.execute(insert_query, data)
    db_connect.db_connection.commit() 
