from sqlalchemy import Column, Integer, Date, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Headline(Base):
    __tablename__ = 'headlines'

    id = Column(Integer, primary_key=True, unique=True)
    date = Column(Date)
    headline = Column(VARCHAR)

    def __init__(self, date, headline):
        self.date = date
        self.headline = headline


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, unique=True)
    url = Column(VARCHAR)
    headline_id = Column(Integer, ForeignKey('headlines.id'))
    headlines = relationship("Headline", backref=backref("urls", uselist=False))

    def __init__(self, url, headlines):
        self.url = url
        self.headline = headlines
