import requests
import json
from fresh_tomatoes import open_movies_page

# PLEASE, INSERT YOUR API KEY BELOW
API_KEY = ""

# The base URLs for the TMDb API, the poster image, and the YouTube trailer.
BASE_URL = "https://api.themoviedb.org/3/movie/"
BASE_POSTER_URL = "https://image.tmdb.org/t/p/w500"
BASE_TRAILER_URL = "https://www.youtube.com/watch?v="


class Movie:
    """A movie is characterized by its title, the URL of its poster image,
    and the URL of its YouTube trailer.
    """
    def __init__(self, title, poster, trailer):
        """Constructor.

        Arguments:
            title {string} -- the title of the movie
            poster {string} -- the URL of the poster image
            trailer {string} -- the URL of the YouTube trailer
        """
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer


def fetch_trailer(movie_id):
    """Given a movie id, retrieves the URL for the movie's YouTube trailer.

    Arguments:
        movie_id {string} -- the movie id

    Returns:
        {string} -- the URL for the movie's YouTube trailer
    """
    url = "%s%s/videos?api_key=%s&language=en-US" % (BASE_URL,
                                                     movie_id, API_KEY)

    response = requests.request("GET", url)
    trailer_list = json.loads(response.content)["results"]
    # We want a YouTube trailer, so from the list of videos, we pick the
    # first one that is a trailer and is hosted on YouTube.
    for trailer in trailer_list:
        if trailer["site"] == "YouTube" and trailer["type"] == "Trailer":
            return "%s%s" % (BASE_TRAILER_URL, trailer["key"])


def main():
    """Fetches a list of popular movies from The Movie Database (TMDb).
    For each movie, extracts its title, the URL of its poster image, and
    the URL of its YouTube trailer. Stores all the movies in a list and
    calls fresh_tomatoes.py to generate a webpage from the list of movies.
    """
    movies = []

    url = "%spopular?page=1&language=en-US&api_key=%s" % (BASE_URL, API_KEY)
    response = requests.request("GET", url)
    movie_list = json.loads(response.content)["results"]

    for movie in movie_list:
        title = movie["title"]
        poster_url = "%s%s" % (BASE_POSTER_URL, movie["poster_path"])
        movie_id = movie["id"]
        trailer_url = fetch_trailer(movie_id)
        # Since we want to be able to play a trailer for each movie, if a
        # movie doesn't have a trailer, we don't add it to the list.
        if trailer_url is not None:
            new_movie = Movie(title, poster_url, trailer_url)
            movies.append(new_movie)

    # Call the fresh_tomatoes.py file to generate a webpage from the
    # list of movies.
    open_movies_page(movies)

if __name__ == "__main__":
    main()
