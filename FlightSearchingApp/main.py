#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
from data_manager import *
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import *
ORIGIN_CITY_IATA = "LON"

notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()

sheet_data = data_manager.get_destination_data()
#print(sheet_data)

if sheet_data[0]["iataCode"]=='':
    from flight_search import FlightSearch
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    #print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, message)