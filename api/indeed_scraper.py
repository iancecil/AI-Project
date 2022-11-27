#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Iancecil Waweru Njoroge 134669
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

def get_url(position, location):
    """Generate url from position and location"""
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = f'https://www.indeed.com/jobs?q={position}&l={location}'
    return url

def get_record(job_card):
    """Extract job data from a single record"""
    
    job_id = job_card.get('data-jk')
    job_title = job_card.h2.text.replace('new','')
    if (job_card.find('span', 'companyName') is not None):
        company = job_card.find('span', 'companyName').text.strip()
    else:
        company = ''
    post_date = job_card.find('span', 'date').text
    today = datetime.today().strftime('%Y-%m-%d')
    summary = job_card.find('div', 'job-snippet').text.strip().replace('\n', ' ')
    job_url = 'https://www.indeed.com' + job_card.get('href')

    record = (job_id,job_title, company, post_date, today, summary, job_url)        
    return record
  

def main(position, location):
    """Run the main program routine"""
    records = []
    url = get_url(position, location)
    
    # extract the job data
    while True:
        
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      cards = soup.find_all('a', 'result')

      for card in cards:
          record = get_record(card)
          records.append(record)
      try:
          # time.sleep(1)
          url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
      except AttributeError:
          break
          
    # export data to pandas dataframe
    print(records)
    results = pd.DataFrame(records)
    results.columns = ['JobID','JobTitle', 'Company', 'PostDate', 'ExtractDate',
                        'Summary', 'JobURL']
    return results