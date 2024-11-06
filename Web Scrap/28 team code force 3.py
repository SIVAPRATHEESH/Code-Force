import pandas as pd
import os
from newspaper import Article
def scrape_and_save(url, codeforce):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text_content = article.text
        
        with open('codeforce.xlsx', 'w', encoding='utf-8') as file:
            file.write(text_content)
                
        print(f"Scraped content from {url} and saved to {filename}")
    except Exception as e:
        print(f"An error occurred while scraping content from {url}: {str(e)}")
df = pd.read_excel('C:/Users/siva/Documents/New folder (2)/codforce.xlsx')

 #enter your file location 
urls = df['URL'].tolist() #give the column name of list of URL in Excel file
url_ids = df['URL_ID'].tolist()
output_directory = 'scraped_content'
os.makedirs(output_directory, exist_ok=True)
for url_id, url in zip(url_ids, urls):
    filename = os.path.join(output_directory, f"{url_id}.txt")  #This saves the output as the text format
    scrape_and_save('url, code force.xlsx')
