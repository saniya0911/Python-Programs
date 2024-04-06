from credentials import *
import requests

SHEET = "users"

def post_new_row(first_name, last_name, email):
    headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}",
        "Content-Type": "application/json",
    }
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=f"{SHEETY_URL}/{SHEET}", headers=headers, json=body)
    response.raise_for_status()

def add_to_club():
    print("Welcome to the Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is your first name ?:\n")
    last_name = input("What is your last name ?:\n")
    email = "1"
    email_validate = "2"
    while(email!=email_validate):
        email = input("What is your email ?:\n")
        email_validate = input("Type your email again.\n")

        if(email == email_validate):
            post_new_row(first_name, last_name, email)
            print("OK. You're in the club!")
    
add_to_club()

