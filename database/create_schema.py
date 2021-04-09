from base import Base
from sqlalchemy.orm import sessionmaker
from database.create_session import get_engine

if __name__ == '__main__':
    engine = get_engine()
    Session = sessionmaker(bind=engine)()

    Base.metadata.create_all(engine)

    Session.commit()
