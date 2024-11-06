import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the URLs of the OEM websites
oem_websites = [
    'https://books.toscrape.com',  # Replace with actual OEM URLs
    # Add more URLs as needed
]

# Predefined email recipients
email_recipients = ['sivapratheesh2004@gmail.com']

# Email settings
smtp_server = 'smtp.example.com'  # Replace with your SMTP server
smtp_port = 587  # SMTP port
smtp_user = 'your_email@example.com'  # Replace with your email
smtp_password = 'your_password'  # Replace with your password

# Function to send email alerts
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = ', '.join(email_recipients)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        text = msg.as_string()
        server.sendmail(smtp_user, email_recipients, text)
        server.quit()
        print(f"Email sent successfully to {', '.join(email_recipients)}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Function to scrape the OEM websites
def scrape_oem_websites():
    for url in oem_websites:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Extract vulnerability information (this part depends on the OEM website's structure)
            vulnerabilities = soup.find_all('div', class_='vulnerability-item')  # Example selector, update as needed
            
            for vulnerability in vulnerabilities:
                severity = vulnerability.find('span', class_='severity').text.strip()
                if severity.lower() in ['critical', 'high']:
                    product_name = vulnerability.find('h2', class_='product-name').text.strip()
                    product_version = vulnerability.find('span', class_='product-version').text.strip()
                    oem_name = vulnerability.find('span', class_='oem-name').text.strip()
                    vuln_description = vulnerability.find('p', class_='description').text.strip()
                    mitigation_url = vulnerability.find('a', class_='mitigation-link')['href']
                    published_date = vulnerability.find('span', class_='published-date').text.strip()
                    unique_id = vulnerability.find('span', class_='cve-id').text.strip()

                    # Prepare email body
                    email_body = f"""
                    Product Name: {product_name}
                    Product Version: {product_version}
                    OEM Name: {oem_name}
                    Severity Level: {severity}
                    Vulnerability: {vuln_description}
                    Mitigation Strategy: {mitigation_url}
                    Published Date: {published_date}
                    Unique ID: {unique_id}
                    """

                    # Send email alert
                    send_email(f"{severity} Vulnerability Alert: {product_name}", email_body)

        except Exception as e:
            print(f"Failed to scrape {url}: {str(e)}")

# Run the scraper
if __name__ == "__main__":
    scrape_oem_websites()
