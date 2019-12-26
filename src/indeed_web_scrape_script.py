import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = 'https://www.indeed.com/jobs?q=data+science&l=Denver%2C+CO#&start=10'

page = requests.get(URL)
soup = BeautifulSoup(page.text, features='html.parser')

def extract_company_from_result(soup):
    companies = []
    for div in soup.find_all(name='div', attrs={'class': 'row'}):
        company = div.find_all(name='span', attrs={'class': 'company'})
        if len(company) > 0:
            for b in company:
                companies.append(b.text.strip())
        else:
            sec_try = div.find_all(name='span', attrs={'class': 'result-link-source'})
            for span in sec_try:
                companies.append(span.text.strip())
    return companies


def extract_job_title_from_result(soup): 
    jobs = []
    for div in soup.find_all(name='div', attrs={'class':'row'}):
        for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
            jobs.append(a['title'])
    return jobs
 
def extract_locations_from_results(soup):
    locations = []
    for div in soup.find_all('div', attrs={'class': 'recJobLoc'}):
        loc = div['data-rc-loc']
        locations.append(loc)
    return locations

def extract_title_company_location(soup):
    jobs = extract_job_title_from_result(soup)
    companies = extract_company_from_result(soup)
    locations = extract_locations_from_results(soup)
    return jobs, companies, locations

df = pd.DataFrame()

jobs, companies, locations = extract_title_company_location(soup)

df['Jobs'] = jobs
df['Companies'] = companies
df['Locations'] = locations