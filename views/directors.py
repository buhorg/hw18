from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        return director_schema.dump(director_service.get_by_id(uid)), 200

