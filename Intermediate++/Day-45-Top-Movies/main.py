from bs4 import BeautifulSoup
import requests

#  Website to be scraped
WEBSITE = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(WEBSITE)
movies_site = response.text

soup = BeautifulSoup(movies_site, 'html.parser')

#  Get all movie titles (nested in a h3 tag)
movie_titles_tags = soup.select(name='h3', class_='title')

#  Iterate through tags and put it in a list
movie_list = [tag.getText() for tag in movie_titles_tags]

#  Reverse the list to get 1-100 -- Can also be done by doing movie_list[::-1]
movie_list.reverse()

#  Open the file and store the movie titles in a txt
with open('movies.txt', mode="w") as file:
    for item in movie_list:
        file.write(f"{item}\n")

