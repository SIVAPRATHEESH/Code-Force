from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't need a browser UI

# Setup Chrome driver path
chrome_driver_path = '/path/to/chromedriver'  # Update with your ChromeDriver path

# Initialize the Chrome driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the BBC website (or any other target website)
url = 'https://www.bbc.com'

# Open the URL
driver.get(url)

try:
    # Wait for the element to load and locate the paragraph with specific attributes
    paragraph = driver.find_element(By.CSS_SELECTOR, "p[data-testid='card-description'].sc-b8778340-4.kYtujW")

    # Print the text of the paragraph
    print(paragraph.text)
except:
    print("Paragraph not found or could not load the content properly.")

# Close the browser
driver.quit()
