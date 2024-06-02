#%%################
##### IMPORTS #####
###################
from dotenv import load_dotenv
import os
import requests

#%%#################
##### LOAD API #####
####################
load_dotenv()  # Load variables from .env file
api_key = os.getenv('API_KEY')

#%%###################
##### VERIFY API #####
######################

base_url = 'https://api.up.com.au/api/v1'
headers = {
    "Authorization": f'Bearer {api_key}'
}

response = requests.get(F'{base_url}/util/ping', headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

#%%########
##### #####
###########

# Accounts

params = {
   'page[size]': 2,
   'filter[accountType]': 'SAVER'
}

accounts = requests.get(f'{base_url}/accounts', headers = headers, params = params)
# accounts = requests.get(f'{base_url}/accounts', headers = headers)
accounts.json()

#%%#####################
##### TRANSACTIONS #####
########################
transactions = requests.get(f'{base_url}/transactions', headers = headers)
transactions.json()