import smtplib
import datetime as dt
import random

SENDER_EMAIL = "" #!enter your email here
SENDER_PASSWORD = "" #! enter your password here

now = dt.datetime.now()
weekday =now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL, 
            to_addrs=SENDER_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



 
 

 
