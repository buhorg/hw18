from dao.model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_id(self, aid):
        return self.session.query(Genre).get_or_404(aid)
