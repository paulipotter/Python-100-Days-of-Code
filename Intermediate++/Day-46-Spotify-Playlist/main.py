import spotipy, requests
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from bs4 import BeautifulSoup

ClientID = 'e1218bfb61f34282bf53ab640f22b69b'


def get_date():
    valid_format = False
    while not valid_format:
        user_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
        date_format = '%Y-%m-%d'
        try:
            valid_format = bool(datetime.strptime(user_date, date_format))
        except ValueError:
            print("Please type the date in this format YYYY-MM-DD")

    # user_date = '2016-03-26'
    billboard_url = f"https://www.billboard.com/charts/hot-100/{user_date}/"
    return billboard_url


def get_soup(billboard_url):
    response = requests.get(billboard_url)
    songs_site = response.text
    soup = BeautifulSoup(songs_site, 'html.parser')
    song_tags = soup.find_all(name='h3', class_="a-no-trucate")

    song_names = [song.getText().strip() for song in song_tags]

    return song_names


def create_playlist():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://example.com",
            client_id='paulipotter',
            client_secret='e1218bfb61f34282bf53ab640f22b69b',
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    print(user_id)

    # Searching Spotify for songs by title
    song_uris = []
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    print(playlist)

    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


url = get_date()
song_list = get_soup(url)
create_playlist()
print(song_list)
