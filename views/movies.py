from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if (director_id is None) and (genre_id is None) and (year is None):
            return movies_schema.dump(movie_service.get_all()), 200
        elif director_id is not None:
            return movies_schema.dump(movie_service.get_director(director_id)), 200
        elif genre_id is not None:
            return movies_schema.dump(movie_service.get_genre(genre_id)), 200
        elif year is not None:
            return movies_schema.dump(movie_service.get_year(year)), 200


    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return req_json, 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        return movie_schema.dump(movie_service.get_by_id(uid)), 200

    def put(self, uid):
        req_json = request.json
        req_json['id'] = uid
        movie = movie_service.update(req_json)
        return movie_schema.dump(movie), 204

    def delete(self, uid):
        movie_service.delete(uid)
        return "", 204