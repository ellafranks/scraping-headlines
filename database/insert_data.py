import glob
import json

from sqlalchemy.orm import sessionmaker

from database.create_session import get_engine
from database.headline import Url, Headline
from utils import url_to_headline, format_url


def insert_data(json_data, session):
    headline = Headline(date=json_data['date'],
                        headline=url_to_headline(json_data['url']))

    url = Url(url=format_url(json_data['url']),
              headlines=True)

    session.add(headline)
    session.add(url)


if __name__ == '__main__':
    engine = get_engine()
    Session = sessionmaker(bind=engine)()

    files = glob.glob('../data/*.json')

    for file in files:
        json_loaded = json.load(open(file))
        for _id, data in json_loaded.items():
            insert_data(json_data=data, session=Session)

    Session.commit()

