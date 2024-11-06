import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = 'https://jovian.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table on the page (assuming there is a table)
table = soup.find('table')

# Extract headers (assuming headers are in <th> tags)
headers = [header.text.strip() for header in table.find_all('th')]

# Extract rows (each row is in a <tr> tag)
rows = table.find_all('tr')[1:]  # Skipping the header row

# Extract data from each row
data = []
for row in rows:
    # Extract data from each cell in the row (each cell is in a <td> tag)
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

# Save the data to a CSV file
csv_filename = 'scraped_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the header row
    writer.writerows(data)     # Write the data rows

print(f"Data has been successfully scraped and saved to {csv_filename}")
