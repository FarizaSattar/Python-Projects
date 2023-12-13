# Birthday Wisher
''' The code allows the user to send a birthday email to anyone. '''

'''
Values to change in code
1) MY_EMAIL in line 19 to your email address.
2) MY_PASSWORD in line 20 to your password. 
3) "[NAME]" in line 42 to the name of the person whose birthday is today.
4) "YOUR EMAIL PROVIDER SMTP SERVER ADDRESS" in line 44 to your SMTP server address.
3) Go to your email provider and make it allow less secure apps.
5) Update birthdays.csv to contain today's month and day.
''' 

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

# Create a dictionary with the birthday dates in the birthday CSV file as keys
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Checking if today's date matches any birthday in the CSV file
if today_tuple in birthdays_dict:
    
    # Obtaining details of the person whose birthday is today
    birthday_person = birthdays_dict[today_tuple]
    
    # Choose a random letter template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Sending the email using SMTP
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )