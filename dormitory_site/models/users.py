from dormitory_site.server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(128), unique=True, nullable=False)
    faculty = db.Column(db.String(128), nullable=False)
    course = db.Column(db.String(128), nullable=False)
    group_number = db.Column(db.String(128), nullable=False)

    def __init__(self, fullname, faculty, course, group_number):
        self.fullname = fullname
        self.faculty = faculty
        self.course = course
        self.group_number = group_number

    def __repr__(self):
        return "<User(fullname='%s', faculty='%s', course='%s', group_number='%s')>" % (
                             self.fullname, self.faculty, self.course, self.group_number)