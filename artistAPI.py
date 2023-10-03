import requests 
import os
from pprint import pprint

artistName1 = "bad bunny"

def get_Artist(artistName):
    #search for the artist
    searchArt = f"https://musicbrainz.org/ws/2/artist?query={artistName}&fmt=json"

    responseArtist = requests.get(searchArt)

    if responseArtist.status_code ==200:
        infoReturn = extract_artist_info(responseArtist.json())
        return infoReturn
    else: 
        return "No artist found"

def extract_artist_info(jsonData):
    realName = jsonData['artists'][0]["aliases"][0]['name']
    #v bgnhmjpprint(realName)
    return realName