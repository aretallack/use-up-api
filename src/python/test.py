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
params = {
    'page[size]': 30,
    'filter[since]':'2024-02-19T00:00:00+10:00',
    }

first_request= requests.get(f'{base_url}/transactions', headers = headers)
transactions = first_request.json()['data']
all_transactions = transactions.copy()
links = first_request.json()['links']

while(links['next'] != None):
    next_request = requests.get(links['next'], headers=headers, params=params)
    next_transaction = next_request.json()['data']
    all_transactions.extend(next_transaction)
    links = next_request.json()['links']