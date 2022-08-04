from flask_restx import Namespace, Resource

from container import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        return genre_schema.dump(genre_service.get_by_id(uid)), 200
