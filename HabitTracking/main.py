import requests
from datetime import datetime
from credentials import *

TODAY = datetime.now()

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today ?"),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"
update_data = {
    "quantity": "4.5"
}
#response = requests.put(url=update_endpoint, json=update_data, headers=headers)
#print(response.text)

#delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)