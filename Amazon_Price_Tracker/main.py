# Amazon Price Tracker
''' The code tracks the price of a product in Amazon. If it goes below a specific number, it will send the user an 
email alert. '''

'''
Values to change in code
  1) BUY_PRICE in line 23 to the price that you want to purchase the item
  2) YOUR_SMTP_ADDRESS in line 32 to your STMP address
  6) YOUR_EMAIL in line 36 to your email address
  7) YOUR_PASSWORD in line 37 to your email address password
  8) YOUR_EMAIL in line 41 to your email address
  9) YOUR_EMAIL in line 42 to your email address
'''

import smtplib

# Extract the title of the product from the webpage
title = soup.find(id="productTitle").get_text().strip()
print(title)  

# Define the target price for purchasing the product
BUY_PRICE = 200  

# Check if the current price is lower than the target price
if price_as_float < BUY_PRICE:
  
  # Send message to user about price change
  message = f"{title} is now {price}"

  # Establish an SMTP connection for sending an email
  with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
    # Initiate a secure connection
    connection.starttls()  
    # Log into the email server
    result = connection.login(YOUR_EMAIL,
                              YOUR_PASSWORD)  
    
    # Send the email with the price alert and the product URL
    connection.sendmail(
        from_addr=YOUR_EMAIL, 
        to_addrs=YOUR_EMAIL, 
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode(
            "utf-8")  
    )
