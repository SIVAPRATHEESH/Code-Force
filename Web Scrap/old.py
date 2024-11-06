import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, csv_filename='scraped_data.csv'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main table on the webpage (you may need to adjust the selector)
        tables = soup.find_all('table')

        # Initialize a list to hold all data
        all_data = []

        # Loop through each table found on the page
        for table in tables:
            # Extract all rows from the table
            rows = table.find_all('tr')

            # Extract data from each row
            for row in rows:
                cells = row.find_all(['th', 'td'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                if row_data:  # Only add non-empty rows
                    all_data.append(row_data)

        if all_data:
            # Save the data to a CSV file
            with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(all_data)
            print(f"Data has been successfully scraped and saved to {csv_filename}")
        else:
            print("No data found on the webpage.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# URL of the webpage to scrape
url = "https://nvd.nist.gov/vuln/vulnerability-status"  # Target Website Link
# Call the function with the desired URL and output CSV filename
scrape_website(url, 'Vulnerability_data.csv')
