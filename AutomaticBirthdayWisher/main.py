import datetime as dt
import pandas
import random
import smtplib
from credentials import *

today = (dt.datetime.now().month,dt.datetime.now().day)
data = pandas.read_csv("myprog/Projects/AutomaticBirthdayWisher/birthdays.csv")

bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in bday_dict:
    birthday_person = bday_dict[today]
    file_path = f"myprog/Projects/AutomaticBirthdayWisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday\n\n{contents}")
