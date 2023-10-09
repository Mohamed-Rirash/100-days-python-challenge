
import smtplib
import datetime as dt
import random

EMAIL = "mail"
PASSWORD = "password"

# calculte select every monday
current_date = dt.date.today()
week_day = current_date.weekday()
if week_day == 0:
    # open file and select a random quote
    with open("day32/quotes.txt") as data:
        quotes = data.readlines()
        quote = random.choice(quotes).strip()
        print(quote)
# send that quote
with smtplib.SMTP("email server ") as connection:
    connection.starttls()
    connection.login(user=EMAIL,password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs="second email",
                        msg=f"subject:monday motovational quote \n\n {quote}")
