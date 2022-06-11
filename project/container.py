from project.setup_db import db

from project.dao import GenreDAO, DirectorDAO, MovieDAO, AuthDAO
from project.services import GenresService, DirectorsService, MoviesService, AuthService

genre_dao = GenreDAO(db.session)
genre_service = GenresService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorsService(director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MoviesService(movie_dao)

auth_dao = AuthDAO(db.session)
auth_service = AuthService(auth_dao)
