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

        # Extract all table rows (adjust selectors based on the structure)
        rows = soup.find_all('tr')

        # If rows are found, extract the data
        if rows:
            data = []
            # Loop through each row
            for row in rows:
                # Extract all cells within the row (th or td)
                cells = row.find_all(['th', 'td'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                if row_data:  # Only add non-empty rows
                    data.append(row_data)

            # Save the data to a CSV file
            with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"Data has been successfully scraped and saved to {'Vulnerability_data.csv'}")
            return data
            
        else:
            print("No data found on the webpage.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# URL of the webpage to scrape
url = "https://education.nationalgeographic.org/resource/nanotechnology/"  #Target Website Link
# Call the function with the desired URL and output CSV filename
scrape_website(url, 'Vulnerability_data.csv')
