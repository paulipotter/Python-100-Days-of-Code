from datetime import datetime
from bs4 import BeautifulSoup
import requests
valid_format = False
# while not valid_format:
#     user_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
#     date_format = '%Y-%m-%d'
#     try:
#         valid_format = bool(datetime.strptime(user_date, date_format))
#     except ValueError:
#         print("Please type the date in this format YYYY-MM-DD")
user_date = '2016-03-26'
billboard_url = f"https://www.billboard.com/charts/hot-100/{user_date}/"

response = requests.get(billboard_url)
songs_site = response.text
soup = BeautifulSoup(songs_site, 'html.parser')
song_tags = song_tags = soup.find_all(name='h3', class_="a-no-trucate")

song_names = [song.getText().strip() for song in song_tags]

print(song_names)