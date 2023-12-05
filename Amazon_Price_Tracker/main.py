# Amazon Price Tracker

''' The code checks the price of a product on Amazon, compares it with a predefined price, and if the current 
price falls below the set value, it sends an email alert with the product title, price, and URL. '''

import smtplib

# Extracting the title of the product from the webpage
title = soup.find(id="productTitle").get_text().strip()
print(title)  # Printing the title of the product

BUY_PRICE = 200  # Defining the target price for purchasing the product

# Checking if the current price is lower than the predefined target price
if price_as_float < BUY_PRICE:
    # Composing the message for the price alert
    message = f"{title} is now {price}"
    
    # Establishing an SMTP connection for sending an email
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()  # Initiating a secure connection
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)  # Logging into the email server
        # Sending the email with the price alert and the product URL
        connection.sendmail(
            from_addr=YOUR_EMAIL,  # Sender's email address
            to_addrs=YOUR_EMAIL,  # Receiver's email address
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")  # Email content with subject and message
        )
