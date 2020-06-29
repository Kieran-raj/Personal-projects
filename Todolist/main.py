from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    date = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def menu():
    options = input('1) Today\'s tasks\n2) Add task\n0) Exit\n')
    if options == '1':
        get_task()
    elif options == '2':
        add_task()
    else:
        print('\nBye!\n')
        exit()


def add_task():
    new_task = input('Enter task\n')
    new_entry = Table(task=new_task)
    session.add(new_entry)
    session.commit()
    print('The task has been added!\n')
    menu()


def get_task():
    rows = session.query(Table).all()
    if len(rows) > 0:
        for row in rows:
            print(f'\n{row.id}. {row.task}')
            menu()
    else:
        print('\nToday:\nNothing to do!\n')
        menu()


menu()
