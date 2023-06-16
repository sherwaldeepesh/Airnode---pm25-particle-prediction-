import json
# to get average values

import requests

url = "https://api.openaq.org/v2/averages?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-29T15%3A10%3A00%2B00%3A00&limit=100&page=1&offset=0&sort=desc&group=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)


# to get cities

import requests

url = "https://api.openaq.org/v2/cities?limit=100&page=1&offset=0&sort=asc&country=IN&order_by=city"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

cities_details = json.loads(response.text)


# to get countries

import requests

url = "https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

country_details = json.loads(response.text)

# Provide a single country by country id

import requests

url = "https://api.openaq.org/v2/countries/IN?limit=200&page=1&offset=0&sort=asc&order_by=country"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

single_country_details = json.loads(response.text)


# provide a list of location

import requests

url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=IN&order_by=lastUpdated&sensorType=low-cost%20sensor&dumpRaw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

locations_details = json.loads(response.text)

# get single location by location id

import requests

url = "https://api.openaq.org/v2/locations/8039?limit=100&page=1&offset=0&sort=desc&radius=1000&order_by=lastUpdated&dumpRaw=false&date_from=2023-05-31&date_to=2023-06-01"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

one_locations_details = json.loads(response.text)


# Provides a list of locations with latest measurements

import requests

url = "https://api.openaq.org/v2/latest?limit=100&page=1&offset=0&sort=desc&radius=1000&country=IN&order_by=lastUpdated&dumpRaw=true"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

location_latest_measurement = json.loads(response.text)

#single location with latest measurements

import requests

url = "https://api.openaq.org/v2/latest/66673?limit=100&page=1&offset=0&sort=desc&radius=1000&order_by=lastUpdated&dumpRaw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

lst_location_latest_measurement = json.loads(response.text)

#get manufacturares

import requests

url = "https://api.openaq.org/v2/manufacturers"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

manufacturers_list = json.loads(response.text)

#list of sensor models
import requests

url = "https://api.openaq.org/v2/models"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

sensor_models_list = json.loads(response.text)



#get measurements

import requests
url = "https://api.openaq.org/v2/measurements?location_id=8039&parameter=pm25&date_from=2023-05-31&date_to=2023-06-01&limit=1000&page=1&order_by=datetime"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)
measurements_list = json.loads(response.text)








