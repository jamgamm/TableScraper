import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30/2022'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tables = soup.find('table', class_ = 'tablesaw')

df = pd.read_html(str(tables))
df = pd.DataFrame(df[0])

df = df.drop(["Pos","Height","Weight","Age",'Pre-Draft Team',"Draft Yr","YOS"], axis = 1)
df.to_excel('playerOfWeek.xlsx')
