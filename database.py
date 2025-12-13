from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

engine = create_engine('postgresql://postgres:Root_1234@localhost/delivery_db', echo=True)

session = sessionmaker(autocommit=False,
                       autoflush=False, bind=engine)

Base = declarative_base()
