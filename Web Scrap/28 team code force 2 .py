import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = 'https://books.toscrape.com'
try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find product listings (adjust the selectors based on the website's structure)
    products = soup.find_all('article', class_='product_pod')

    if products:
        data = []
        # Loop through each product and extract details
        for product in products:
            product_name = product.h3.a['title'].strip() if product.h3.a else 'No Name'
            product_price = product.select_one('p.price_color').text.strip() if product.select_one('p.price_color') else 'No Price'

            # Append the extracted data to the list
            data.append([product_name, product_price])

        # Define the CSV file name
        csv_filename = 'Website datas.csv'
        
        # Save the data to a CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the headers
            writer.writerow(['Book Title', 'Price'])
            # Write the data rows
            writer.writerows(data)

        print(f"Data has been successfully scraped and saved to {csv_filename}")
    else:
        print("No products found on the webpage.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
