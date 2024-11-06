import requests
from bs4 import BeautifulSoup
import csv
# URL of the webpage to scrape
url = 'https://www.bbc.com'

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find product listings (adjust the selectors based on the website's structure)
    products = soup.find_all('div', class_='product-item-info')

    if products:
        data = []
        # Loop through each product and extract details
        for product in products:
            product_name = product.find('a', class_='product-item-link').text.strip()
            product_price = product.find('span', class_='price').text.strip()

            # Append the extracted data to the list
            data.append([product_name, product_price])

        # Define the CSV file name
        csv_filename = 'acer_products.csv'
        
        # Save the data to a CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the headers
            writer.writerow(['Product Name', 'Price'])
            # Write the data rows
            writer.writerows(data)

        print(f"Data has been successfully scraped and saved to {csv_filename}")
    else:
        print("No products found on the webpage.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
