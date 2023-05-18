import imdb
import urllib.request
from PIL import Image

def get_cover(film_name):
    # create an IMDbPY instance
    ia = imdb.IMDb()

    # search for the movie by title
    movie_title = film_name
    movies = ia.search_movie(movie_title)

    # get the first result and its ID
    movie_id = movies[0].getID()

    # retrieve the movie details using the ID
    movie = ia.get_movie(movie_id)

    # get the URL of the movie cover image
    cover_url = movie.get('full-size cover url')

    # download the image and save it to disk
    urllib.request.urlretrieve(cover_url, "recom_app/static/"+film_name+".jpg")

"""     # open the downloaded image using Pillow
    image = Image.open("cover.jpg")

    # show the image
    image.show()

    return cover_url """

if __name__ == "__main__":
    get_cover("The Dark Knight")