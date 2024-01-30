import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "<email>@gmail.com"
MY_PASSWORD = "<app password>"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    num = random.randint(1, 3)
    letter_path = f"./letter_templates/letter_{num}.txt"
    with open(letter_path) as letter:
        content = letter.read()
        birthday_letter = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday {birthday_person["name"]}\n\n{birthday_letter}")
        