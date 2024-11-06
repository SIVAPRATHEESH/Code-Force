import requests
from bs4 import BeautifulSoup

# URL of the BBC website
url = 'https://www.youtube.com/watch?v=tmAISS8WkHo'

# Send a GET request to the BBC website
response = requests.get(url)
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all headline elements (this may vary depending on the website structure)
    # Commonly, headlines are within <h3> tags or similar
    p = soup.find_all('p')
    # print(headlines)

    # Print out the text of each headline
    for index, headline in enumerate(p):
        print(f"{index + 1}. {headline.get_text(strip=True)}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
