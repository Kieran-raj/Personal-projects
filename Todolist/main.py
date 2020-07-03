# look at adding a start time and a finish time likely be just new columns, which would go into the class


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    date = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def menu():
    options = input('1) Today\'s tasks\n2) Week\'s tasks\n3) All tasks\n'
                    '4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n')
    if options == '1':
        get_today()
    elif options == '2':
        get_week()
    elif options == '3':
        get_all()
    elif options == '4':
        get_missed()
    elif options == '5':
        add_task()
    elif options == '6':
        delete_list()
    else:
        print('\nBye!\n')
        exit()


def add_task():
    new_task = input('Enter task\n')
    new_deadline = input('Enter deadline\n')
    if new_deadline != '':
        new_entry = Table(task=new_task, date=datetime.strptime(new_deadline, '%Y-%m-%d').date())
    else:
        new_entry = Table(task=new_task)
    session.add(new_entry)
    session.commit()
    print('The task has been added!\n')
    menu()


def get_today():
    i = 1
    today = datetime.today().date()
    rows = session.query(Table).filter(Table.date == today).all()
    if len(rows) > 0:
        print(f'\nToday {today.day} {today.strftime("%b")}:')
        for row in rows:
            print(f'{i}. {row.task}')
            i += 1
        print('\n')
        menu()
    else:
        print(f'\nToday {today.day} {today.strftime("%b")}:\nNothing to do!\n')
        menu()


def get_week():
    today = datetime.today().date()
    for n in range(7):
        future_days = today + timedelta(days=n)
        rows = session.query(Table).filter(Table.date == future_days).all()  # produces a list
        if len(rows) > 0:
            print(f'\n{future_days.strftime("%A")} {future_days.day} {future_days.strftime("%b")}:')
            i = 1
            for row in rows:
                print(f'{i}. {row.task}')
                i += 1
        else:
            print(f'\n{future_days.strftime("%A")} {future_days.day} {future_days.strftime("%b")}:\nNothing to do!\n')
    print("\n")
    menu()


month = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
            7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


def get_all():
    dates = []
    print('\nAll tasks:')
    rows = session.query(Table).all()
    for row in rows:
        dates.append(row.date)
    i = 1
    for n in list(dict.fromkeys(sorted(dates))):
        new_rows = session.query(Table).filter(Table.date == n).all()
        for row in new_rows:
            row_month = month[row.date.month]
            print(f'{i}. {row.task}. {row.date.day} {row_month}')
            i += 1
    print('\n')
    menu()


def get_missed():
    today = datetime.today().date()
    rows = session.query(Table).filter(Table.date < today).all()
    i = 1
    print(f'Missed tasks:')
    if len(rows) > 0:
        for row in rows:
            row_month = month[row.date.month]
            print(f'{i}. {row}. {row.date.day} {row_month}')
            i += 1
    else:
        print(f'Nothing is missed!')
    print('\n')
    menu()


def delete_list():
    today = datetime.today().date()
    rows = session.query(Table).filter(Table.date < today).all()
    i = 1
    length = len(rows)
    if length > 0:
        print('Chose the number of the task you want to delete:')
        for row in rows:
            row_month = month[row.date.month]
            tasks = f'{i}. {row} {row.date.day} {row_month}'
            print(tasks)
            i += 1
        delete_choice(rows)
    else:
        print('No tasks to delete')
        menu()


def delete_choice(rows):
    choice = int(input()) - 1
    specific_row = rows[choice]
    print(specific_row)
    session.delete(specific_row)
    session.commit()
    print('The task has been deleted!')
    menu()


menu()

