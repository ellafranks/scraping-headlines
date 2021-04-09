from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    return create_engine('postgresql://ella.franks:test@localhost:5431/news')
