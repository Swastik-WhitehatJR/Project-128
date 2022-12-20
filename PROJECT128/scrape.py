from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(URL)
soup = BeautifulSoup(page.text,'html.parser')
star = soup.find_all('table', {"class":"wikitable sortable"})

temp_list= []
rows = star[1].find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

names = []
distance =[]
mass = []
radius =[]

for i in range(1,len(temp_list)):
    names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])


headers = ['StarName','Distance','Mass','Radius']  
df = pd.DataFrame(list(zip(names,distance,mass,radius)),columns=['Star_name','distance','mass','radius'])
df.to_csv('data.csv', index=True, index_label="id")