from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    release_date = Column(DateTime, nullable=False)
    url = Column(String(128), nullable=False)

class Ratings(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    movie_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)



### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
