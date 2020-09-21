from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean, VARCHAR
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    task = Column(String)
    date = Column(Date, default=datetime.today().date())
    done = Column(Boolean, default=False)

    def __repr__(self):
        return self.task


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_name = Column(VARCHAR)
    user_id = Column(Integer)
    logged_in = Column(Integer)

    def __repr__(self):
        return self.user_name


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


