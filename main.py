import random
import os.path
import smtplib
import datetime as dt
import pandas as pandas

# region MAIL AUTH
email = "lfcamachodev@gmail.com"
password = input("Enter Password: ")
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
SSL_PORT = 465
# endregion MAIL AUTH

now = dt.datetime.now()
day_of_week = now.weekday()
letters = os.listdir("letter_templates")

birthday_data = pandas.read_csv("birthdays.csv")
found = birthday_data.loc[(birthday_data['month'] == now.month) & (birthday_data['day'] == now.day)]
found_name = found.name.values[0]
found_email = found.email.values[0]

if not found.empty:
    chosen_letter = random.choice(letters)
    with open(f"letter_templates/{chosen_letter}", "r") as let:
        letter_data = let.read()
        final_letter = letter_data.replace("[NAME]", found_name)

    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        selected_quote = random.choice(quotes)

    with smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT) as connection:  # connection.starttls() # used without SSL
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=f"{found_email}",
            msg=f"Subject: Happy Birthday {found_name}!\n\n "
                f"{final_letter}\n\n\n"
                f"----------------------------\n"
                f"{selected_quote}")
