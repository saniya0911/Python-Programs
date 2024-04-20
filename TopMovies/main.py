URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

import requests 
from bs4 import BeautifulSoup

response = requests.get(url=URL)
movies_website = response.text
soup = BeautifulSoup(movies_website, "html.parser")

movies = soup.find_all(name="h3", class_ = "title")
movie_titles = [movie.getText() for movie in movies]
movies = movie_titles[::-1]

with open("myprog/Projects/TopMovies/movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")