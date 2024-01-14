# Web Scraper
''' The code creates a web scraper for the user. '''

import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find elements containing book information (replace these selectors with the actual ones on the website)
        books = soup.find_all('div', class_='book-info')  # Replace 'div' and 'class_' with actual selectors

        # Initialize an empty list to store the extracted data
        book_data = []

        # Extract information for each book
        for book in books:
            # Example: Extracting book title, author, and price (replace these with actual data)
            title = book.find('h2', class_='book-title').text.strip()  # Replace with the actual title selector
            author = book.find('p', class_='author').text.strip()  # Replace with the actual author selector
            price = book.find('span', class_='price').text.strip()  # Replace with the actual price selector

            # Store the extracted data in a dictionary
            book_info = {
                'Title': title,
                'Author': author,
                'Price': price
                # Add more fields as needed
            }

            # Append the book information to the list
            book_data.append(book_info)

        return book_data
    else:
        print("Failed to retrieve the webpage.")
        return None

# URL of the website to scrape (replace with the actual website URL)
url_to_scrape = 'https://example.com/books'

# Call the function and pass the URL
scraped_data = scrape_books(url_to_scrape)

if scraped_data:
    # Display the scraped data
    for book in scraped_data:
        print(f"Title: {book['Title']}")
        print(f"Author: {book['Author']}")
        print(f"Price: {book['Price']}")
        print("\n")
else:
    print("No data scraped.")
