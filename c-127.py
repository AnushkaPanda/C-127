from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('C:/Users/NXG/Downloads/class-127/chromedriver')
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=['Name','Light-years_from_earth','Planet_mass','Stellar_magnitude','Discovery_date']
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs = {'class','exoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp_list=[]
            for index,li_tg in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tg.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tg.contents[0])
                    except:
                        temp_list.append('')
            planet_data.append(temp_list)
        browser.find_element('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scaper.csv','w')as f:
        csvw = csv.writer(f)
        csvw.writerow(headers)
        csvw.writerow(planet_data)

scrape()


        
