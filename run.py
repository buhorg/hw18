from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from data.data import data
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns

from views.movies import movie_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    configurate_app(application)
    create_data(application, db)
    return application


def configurate_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()
        movies = data['movies']
        directors = data['directors']
        genres = data['genres']
        movies_list = []
        directors_list = []
        genres_list = []
        for item in movies:
            movies_list.append(Movie(**item))
        for item in directors:
            directors_list.append(Director(**item))
        for item in genres:
            movies_list.append(Genre(**item))
        movies_list.extend(directors_list)
        movies_list.extend(genres_list)
        with db.session.begin():
            db.session.add_all(movies_list)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(debug=True)
