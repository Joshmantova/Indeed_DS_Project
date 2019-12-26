import indeed_web_scrape_script as iwss
import time
from bs4 import BeautifulSoup
import requests

starting_url = 'https://www.indeed.com/jobs?q=data+science&l=Denver%2C+CO&limit=50&radius=25'
start = [num for num in range(50, 251, 50)]
url_list = [starting_url]

for i in start:
    base_url = starting_url
    page_num = f'&start={i}'
    base_url += page_num
    url_list.append(base_url)

for url in url_list:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='html.parser')
    job_temp, companies_temp, locations_temp = iwss.extract_title_company_location(soup)