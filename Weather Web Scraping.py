import pandas as pd

import requests

from bs4 import BeautifulSoup

page = requests.get('https://www.worldweatheronline.com/lang/en-in/vizag-weather/andhra-pradesh/in.aspx')

soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='days5_section')

items = week.find_all(class_='carousel-cell well text-center')


# print(items[0].find(text=True))

# print(items[0].find('img')['title'])

# print(items[0].find('strong').get_text())

dates_list = [item.find(text=True) for item in items]

descriptions_list = [item.find('img')['title'] for item in items]

temperatures_list = [item.find('strong').get_text() for item in items]

# print(dates_list)
# print(descriptions_list)
# print(temperatures_list)

weather_stuff = pd.DataFrame(
	{
	'dates': dates_list,
	'descriptions': descriptions_list,
	'temperatures': temperatures_list,
	})

print(weather_stuff)

weather_stuff.to_csv('vizag weather.csv')