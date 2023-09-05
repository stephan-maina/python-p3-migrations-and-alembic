from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

# Replace 'your_database_uri' with your actual database URI (e.g., 'sqlite:///mydb.db')
engine = create_engine('your_database_uri')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
