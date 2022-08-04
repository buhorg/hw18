from dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_id(self, aid):
        return self.session.query(Director).get_or_404(aid)
