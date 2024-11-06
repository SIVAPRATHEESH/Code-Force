import pandas as pd
import os
from newspaper  import Article

def scrape_and_save(url,codeforce):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text_content = article.text
        
        with open(codeforce, 'w', encoding='utf-8') as file:
            file.write(text_content)
                
        print(f"Scraped content from {url} and saved to {codeforce}")
    except Exception as e:
        print(f"An error occurred while scraping content from {url}: {str(e)}")
        
# Load the Excel file
df = pd.read_excel(r'C:\Users\siva\Documents\New folder (2)\codeforce.xlsx')
# df = pd.read_excel('codeforce.xlsx')  # Enter your file location 
urls = df['URL'].tolist()  # Give the column name of the list of URLs in Excel file
url_ids = df['URL_ID'].tolist()  # Give the column name of URL IDs in Excel file

# Create the output directory if it doesn't exist
output_directory = r'C:\Users\siva\Desktop\Web Scrap'
os.makedirs(output_directory, exist_ok=True)

# Loop through URLs and save their content
for url_id, url in zip(url_ids, urls):
    codeforce = os.path.join(output_directory, f"{url_id}.txt")  # This saves the output as a text file
    scrape_and_save(url,"codeforce")
