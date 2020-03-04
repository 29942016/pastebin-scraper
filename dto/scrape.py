class Scrape:
    def __init__(self, _id, user, misc):
        self._id = _id
        self.user = user
        self.misc = misc

    def __str__(self):
        return str(self._id)
