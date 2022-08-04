from dao.director import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, uid):
        return self.dao.get_by_id(uid)