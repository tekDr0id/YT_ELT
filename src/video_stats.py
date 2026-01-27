import requests
import json
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")  # must run before os.getenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_HANDLE = "OpenAI"

def get_playlist_id():   

    try:    
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={YOUTUBE_API_KEY}"

        response = requests.get(url)
        response.raise_for_status()



        data = response.json()
        #print(json.dumps(data,indent=4s))

        channel_items = data['items'][0]
        channel_playlistID = channel_items['contentDetails']['relatedPlaylists']['uploads']

        #print(channel_playlistID)

        return channel_playlistID

    except requests.exceptions.RequestException as e: 
        raise e

if __name__ == "__main__":
    print("get_playslist_id will be executed")
    get_playlist_id()
else:
    print("get_playlist_id will not be executed")
