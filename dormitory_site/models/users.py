from dormitory_site.models.base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(128), unique=True, nullable=False)
    faculty = Column(String(128), nullable=False)
    course = Column(String(128), nullable=False)
    group_number = Column(String(128), nullable=False)

    def __init__(self, fullname, faculty, course, group_number):
        self.fullname = fullname
        self.faculty = faculty
        self.course = course
        self.group_number = group_number

    def __repr__(self):
        return "<User(fullname='%s', faculty='%s', course='%s', group_number='%s')>" % (
                             self.fullname, self.faculty, self.course, self.group_number)
