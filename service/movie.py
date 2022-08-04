from dao.movie import MovieDao


class MovieService:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, mid):
        return self.dao.get_by_id(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def delete(self, mid):
        return self.dao.delete(mid)

    def get_director(self, uid):
        return self.dao.get_director(uid)

    def get_genre(self, uid):
        return self.dao.get_genre(uid)

    def get_year(self, year):
        return self.dao.get_year(year)