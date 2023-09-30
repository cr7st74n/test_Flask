import requests 

def get_Artist():
    # URL to thet the discography
    ArtistURL = "https://genius-song-lyrics1.p.rapidapi.com/artist/details/"

    queryString = {"id", "344497"}

    headers = {
	"X-RapidAPI-Key": "c20c242974mshe8cc858d0dfe43ep152a87jsn8e4eee20a17a",
	"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    responseArtist = requests.get(ArtistURL, headers=headers, params=queryString)

    return responseArtist

def extract_artist_info(jsonData):

    return {
        
    }