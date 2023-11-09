from google.cloud import ndb
import requests
import json

omdb_api_key= f'f9707c80'

class MovieFetcher():
    @classmethod
    def fetch_movies(self):
        f = open('movieList.json')
        data = json.load(f)
        for title in data['movies']: 
            url = f"http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}"
            response = requests.get(url)
            data = response.json()
            entity = Movie(
                title=data.get("Title"),
                year=data.get("Year"),
                director=data.get("Director")
            )
            entity.put()
        print(f"The database has been populated.")
        f.close()
        # ancestor_key = ndb.Key("BriteGroup", "movies")
        # query = Movie.query(ancestor=ancestor_key)
        # # names = [c.test for c in query]
        # if not query:
            # for _ in range(100):
            # self.get_movie_data()
    
class Movie(ndb.Model):
    title = ndb.StringProperty()
    year = ndb.StringProperty()
    director = ndb.StringProperty()

if __name__ == '__main__':
    client = ndb.Client()
    with client.context():
        query = Movie.query()
        if not list(query.fetch(limit=1)):
            omdb_fetcher = MovieFetcher()
            omdb_fetcher.fetch_movies()
        else:
            print(f"Database is already populated. No changes were made.")
