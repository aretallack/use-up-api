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

url = "https://api.up.com.au/api/v1/util/ping"
headers = {
    "Authorization": f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")