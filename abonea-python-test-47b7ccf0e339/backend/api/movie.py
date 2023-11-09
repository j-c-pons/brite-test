import time

from backend.wsgi import remote, messages, message_types

from backend import api, movies
from backend.oauth2 import oauth2, Oauth2
from backend.swagger import swagger

class GetMovieRequest(messages.Message):
    id = messages.StringField(1, required=True)

class GetMovieResponse(messages.Message):
    id = messages.StringField(1)
    name = messages.StringField(2)
    
@api.endpoint(path="movies", title="Movie API")
class Movie(remote.Service):
    @swagger("Get a movie")
    #@oauth2.required()
    @remote.method(GetMovieRequest, GetMovieResponse)
    def get(self, request):
        u = movies.Movie.get(request.id)
        return GetMovieResponse(
            id=u.id,
            name=u.name
        )