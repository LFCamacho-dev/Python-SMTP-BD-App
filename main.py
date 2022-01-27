import random
import os.path
import smtplib
import datetime as dt
import pandas as pandas

# region MAIL AUTH
email = "l*********@gmail.com"
password = "********"
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
SSL_PORT = 465
# endregion MAIL AUTH

now = dt.datetime.now()
today_date = f"{now.month} - {now.day}"
letters = os.listdir("letter_templates")

birthday_data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
for bd in birthday_data:
    birth_date = f"{bd['month']} - {bd['day']}"

    if today_date == birth_date:

        chosen_letter = random.choice(letters)
        with open(f"letter_templates/{chosen_letter}", "r") as let:
            letter_data = let.read()
            final_letter = letter_data.replace("[NAME]", bd['name'])

        with open("quotes.txt", "r") as file:
            quotes = file.readlines()
            selected_quote = random.choice(quotes)

        with smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT) as connection:  # connection.starttls() # used without SSL
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=f"{bd['email']}",
                msg=f"Subject: Happy Birthday {bd['name']}!\n\n "
                    f"{final_letter}\n\n\n"
                    f"----------------------------\n"
                    f"{selected_quote}")

        print(f"Birthday email sent to {bd['name']}, ({bd['year']} - {birth_date})")
