# Music Time Machine
''' The code creates a playlist and add songs to it from the user's Spotify account. '''

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# Fetching Billboard 100 data based on the provided date
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)  
# Parsing HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')  
# Selecting HTML elements containing song names
song_names_spans = soup.select("li ul li h3")  
# Extracting song names
song_names = [song.getText().strip() for song in song_names_spans]  

# Spotify Authentication - Creating a Spotify client object
sp = spotipy.Spotify(  
    # Authenticating via OAuth
    auth_manager=SpotifyOAuth(  
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        # Replace with your Spotify Client ID
        client_id='YOUR CLIENT ID',  
        # Replace with your Spotify Client Secret
        client_secret='YOUR CLIENT SECRET',  
        show_dialog=True,
        cache_path="token.txt"
    )
)
# Fetching the user's Spotify ID
user_id = sp.current_user()["id"]  
print(user_id)

# Searching Spotify for songs by title
song_uris = []
# Extracting the year from the provided date
year = date.split("-")[0]  
for song in song_names:
    # Searching for tracks on Spotify by song title and year
    result = sp.search(q=f"track:{song} year:{year}", type="track")  
    print(result)
    try:
        # Extracting the URI of the first search result
        uri = result["tracks"]["items"][0]["uri"]  
         # Adding the URI to the list of song URIs
        song_uris.append(uri) 
    except IndexError:
        # Handling songs not found on Spotify
        print(f"{song} doesn't exist in Spotify. Skipped.")  

# Creating a private playlist named after the input dates
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)  
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)  # Adding found songs to the newly created playlist
