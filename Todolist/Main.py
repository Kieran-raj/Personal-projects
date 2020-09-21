from Users import *


def get_user_id(user_name):
    rows = session.query(Users).filter(Users.user_name == user_name).all()
    for row in rows:
        return row.user_id


def start_up():
    outof_date()
    rows_up = session.query(Table).filter(Table.done == 1).all()
    for row_up in rows_up:
        session.delete(row_up)
        session.commit()
    menu()


def outof_date():
    today = datetime.today().date()
    past_week = today - timedelta(days=4)
    rows_outof = session.query(Table).filter(Table.date < past_week).all()
    for row_outof in rows_outof:
        session.delete(row_outof)
        session.commit()


def menu():
    options = input('''\nMain Menu:\n1) Today\'s tasks\n2) Week\'s tasks\n3) All tasks\n
4) Missed tasks\n5) Add task\n
s) Settings\n
l) Log out
0) Exit\n''')
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
    elif options.lower() == 's':
        settings()
    elif options.lower() == 'l':
        log_out(user_id)
    elif options == '0':
        print('\nBye!\n')
        exit()
    else:
        print('Invalid Input')


def add_task():
    new_task = input('Enter task\n')
    new_deadline = input('Enter deadline (YYYY-MM-DD or "today")\n').lower()
    if new_deadline != 'today':
        new_entry = Table(user_id=user_id, task=new_task, date=datetime.strptime(new_deadline, '%Y-%m-%d').date())
    else:
        new_entry = Table(user_id=user_id, task=new_task)
    session.add(new_entry)
    session.commit()
    print('\nThe task has been added!')
    menu()


def get_today():
    i = 1
    today = datetime.today().date()
    rows_today = session.query(Table).filter(Table.user_id == user_id).filter(Table.date == today).all()
    if len(rows_today) > 0:
        print(f'\nToday {today.day} {today.strftime("%b")}:')
        for row_today in rows_today:
            if row_today.done:
                print(f'{i}. {row_today.task} - Done')
            else:
                print(f'{i}. {row_today.task} - Unfinished')
            i += 1
        today_menu(rows_today)
    else:
        print(f'\nToday {today.day} {today.strftime("%b")}:\nNothing to do!\n')
        menu()


def get_week():
    today = datetime.today().date()
    for n in range(7):
        future_days = today + timedelta(days=n)
        rows = session.query(Table).filter(Table.user_id == user_id).filter(Table.date == future_days).all()
        if len(rows) > 0:
            print(f'\n{future_days.strftime("%A")} {future_days.day} {future_days.strftime("%b")}:')
            i = 1
            for row in rows:
                print(f'{i}. {row.task}')
                i += 1
        else:
            print(f'\n{future_days.strftime("%A")} {future_days.day} {future_days.strftime("%b")}:\nNothing to do!\n')
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
    if len(dates) > 0:
        for n in list(dict.fromkeys(sorted(dates))):
            new_rows = session.query(Table).filter(Table.user_id == user_id).filter(Table.date == n).all()
            for row in new_rows:
                row_month = month[row.date.month]
                if row.done:
                    print(f'{i}. {row.task}. {row.date.day} {row_month} - Done')
                else:
                    print(f'{i}. {row.task}. {row.date.day} {row_month} - Unfinished')
                i += 1
    else:
        print('Nothing to do!')
    print('\n')
    option = input('1) Delete task\n2) Back\n')
    if option == '1':
        delete_list(rows)
    elif option == '2':
        menu()


def get_missed():
    today = datetime.today().date()
    rows = session.query(Table).filter(Table.user_id == user_id).filter(Table.date < today).all()
    i = 1
    print(f'\nMissed tasks:')
    if len(rows) > 0:
        for row in rows:
            row_month = month[row.date.month]
            print(f'{i}. {row}. {row.date.day} {row_month}')
            i += 1
    else:
        print(f'Nothing is missed!')
    menu()


def delete_list(rows):
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
        print('\nNo tasks to delete\n')
        menu()


def delete_choice(rows):
    choice = int(input()) - 1
    specific_row = rows[choice]
    session.delete(specific_row)
    check = input('Are you sure you want to delete the task? (Y/N)\n').lower()
    if check == 'y':
        session.commit()
        print('The task has been deleted!\n')
        menu()
    else:
        menu()


def today_menu(rows_today):
    while True:
        option = input('\nOptions:\n1) Mark as done\n2) Back\n0) Exit\n')
        if option == '1':
            done(rows_today)
        elif option == '2':
            menu()
        elif option == '0':
            print('\nBye!')
            exit()
        else:
            print('\nInvalid option')


def done(rows):
    choice = int(input('\nSelect the number(s) of the task completed: ')) - 1
    row_id = rows[choice].id
    session.query(Table).filter(Table.id == row_id).update({Table.done: True})
    session.commit()
    print('Marked as done')
    menu()


def settings():
    response = input('\n1) Delete profile\n2) Update profile\n3) Back\n0) Exit\n')
    if response.lower() == '1':
        delete_user(user_name, user_id)
    elif response == '3':
        menu()
    elif response == '2':
        update_user(user_id)
        settings()
    elif response == '0':
        print('\nBye!')
        exit()


if __name__ == '__main__':
    while True:
        user_name = login()
        if not user_name == False:
            user_id = get_user_id(user_name)
            start_up()

