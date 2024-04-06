import requests
from credentials import SHEETY_URL, SHEET_TOKEN
SHEET = "prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {SHEET_TOKEN}",
        }
        sheety_response = requests.get(url = f"{SHEETY_URL}/{SHEET}", headers=headers)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        headers = {
            "Authorization": f"Bearer {SHEET_TOKEN}",
        }
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/{SHEET}/{city['id']}",
                headers=headers,
                json=new_data
            )

    def get_customer_emails(self):
        customers_endpoint = f"{SHEETY_URL}/{SHEET}"
        headers = {
            "Authorization": f"Bearer {SHEET_TOKEN}",
        }
        response = requests.get(url=customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
            