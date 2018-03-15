from datetime import date
from .model import Wallet
from .model import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite://assignment2.db')
Base.metadata.create_all(engine)
# from common.base import session_factory

def session_factory():
    from sqlalchemy.orm import sessionmaker
    DBsession = sessionmaker(bind=engine)
    return DBsession()

def create_wallet():
    session = session_factory()
    wallet = Wallet("012345", 1000,"")
    session.add(wallet)
    session.close()


def get_wallet():
    session = session_factory()
    wallet_query = session.query(Wallet)
    session.close()
    return wallet_query.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()

    for person in people:
        print(f'{person.name} was born in {person.date_of_birth}')