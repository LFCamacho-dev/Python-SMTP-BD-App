import smtplib


my_email = "lfcamachodev@gmail.com"
my_password = input("Password: ")
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
SSL_PORT = 465

with smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT) as connection:
    # connection.starttls() # used without SSL
    connection.login(user=my_email, password=my_password)

    connection.sendmail(from_addr=my_password,
                        to_addrs="luisfernandoca@yahoo.com",
                        msg="Subject: Hola con SSL!\n\n "
                            "This is the body of my email")


