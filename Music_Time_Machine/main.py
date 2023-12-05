# Music Time Machine

''' The code scrapes Billboard 100 songs for a user-input date, authenticates with Spotify to access user 
data, searches for songs on Spotify based on the scraped song titles, creates a private playlist on Spotify 
named after the input date, and adds the found songs into the newly created playlist. '''

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)  # Fetching Billboard 100 data based on the provided date
soup = BeautifulSoup(response.text, 'html.parser')  # Parsing HTML content using BeautifulSoup
song_names_spans = soup.select("li ul li h3")  # Selecting HTML elements containing song names
song_names = [song.getText().strip() for song in song_names_spans]  # Extracting song names

# Spotify Authentication
sp = spotipy.Spotify(  # Creating a Spotify client object
    auth_manager=SpotifyOAuth(  # Authenticating via OAuth
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='YOUR CLIENT ID',  # Replace with your Spotify Client ID
        client_secret='YOUR CLIENT SECRET',  # Replace with your Spotify Client Secret
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]  # Fetching the user's Spotify ID
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]  # Extracting the year from the provided date
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")  # Searching for tracks on Spotify by song title and year
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]  # Extracting the URI of the first search result
        song_uris.append(uri)  # Adding the URI to the list of song URIs
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")  # Handling songs not found on Spotify

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)  # Creating a private playlist named after the input date
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)  # Adding found songs to the newly created playlist
