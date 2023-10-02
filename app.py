from flask import Flask, render_template ,request
import requests
from artistAPI import get_Artist

app = Flask(__name__)

@app.route('/') #home page
def homepage():
    return render_template('index.html')


@app.route("/get_artist") # will get the artist info from the API
def get_artist_info():
    artist = request.args.get("artist") # safer - return None if no username

    returnUser = get_Artist(artist)

    return render_template('artist.html', artistName= returnUser) # render our data, and send it to the html file to display.
    



if __name__ == '__name__':
    app.run()


