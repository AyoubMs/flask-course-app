from . import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    author = db.Column(db.String(50))
    overview = db.Column(db.String(200))
    link = db.Column(db.String(100))
    image = db.Column(db.String(200))

    def toDict(self):
        return dict(id=self.id, title=self.title, author=self.author, overview=self.overview, url=self.url, image=self.image)