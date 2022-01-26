import random
import smtplib
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "lfcamachodev@gmail.com"
my_password = input("Password: ")
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
SSL_PORT = 465


if day_of_week == 2:
    with open("quotes.txt", "r") as file:
        quotes = (file.readlines())
        selected_quote = random.choice(quotes)

    with smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT) as connection:
        # connection.starttls() # used without SSL
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_password,
                            to_addrs="luisfernandoca@yahoo.com,lfcamachodev@gmail.com",
                            msg=f"Subject: Quote Of The Day\n\n "
                                f"{selected_quote}")

        print(selected_quote + " was sent")





