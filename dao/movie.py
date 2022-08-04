from dao.model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, aid):
        return self.session.query(Movie).get_or_404(aid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        uid = data.get('id')
        self.session.query(Movie).filter(Movie.id == uid).update(data)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()

    def get_director(self, uid):
        return self.session.query(Movie).filter(Movie.director_id == uid).all()

    def get_genre(self, uid):
        return self.session.query(Movie).filter(Movie.genre_id == uid).all()

    def get_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()
