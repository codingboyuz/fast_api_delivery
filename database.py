from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

engine = create_engine('postgresql://postgres:Root_1234@localhost/delivery_db',echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
