from Table_gen import *
import random
global user_name


def user():
    global user_name
    user_name = input('Username: ')
    return user_name


def login():
    global user_name
    login = input('Sign up (u), sign in?(i) or exit: ').lower()
    if login == 'i':
        user_name = user()
        if user_entry(user_name):
            if session.query(Users).filter(Users.logged_in) == 1:
                print('You are already logged in')
                return user_name
            else:
                session.query(Users).filter(Users.user_name == user_name).update({Users.logged_in: 1})
                session.commit()
                print('Logged in')
                return user_name
    elif login == 'u':
        user_name = new_user()
        return user_name
    elif login == 'exit':
        exit()
    else:
        print('Invalid option')
        return False


def user_entry(user_name):
    if session.query(Users).filter(Users.user_name == user_name).all():
        return True
    else:
        print('Account doesn\'t exist!')
        if input('Would you like you to make a new account? (Y/N): ').lower() == 'y':
            length = random.randrange(1, len(user_name))
            user_id = ''.join(random.choices(user_name, k=length)) + str(random.randrange(10))
            new_entry = Users(user_name=user_name, user_id=user_id, logged_in=1)
            session.add(new_entry)
            session.commit()
            print('New user account made')
        else:
            exit()


def new_user():
    global user_name
    user_name = input('Enter username: ')
    while True:
        if session.query(Users).filter(Users.user_name == user_name).all():
            print('Username already taken!')
            user_name = input('Enter different username: ')
        else:
            break
    length = random.randrange(1, len(user_name))
    user_id = ''.join(random.choices(user_name, k=length)) + str(random.randrange(10))
    new_entry = Users(user_name=user_name, user_id=user_id)
    session.add(new_entry)
    session.commit()
    print('Profile created')
    return user_name


def delete_user(user_name, user_id):
    response = input('Are you sure you want to delete your profile? (Y/N) ')
    if response.lower() == 'y':
        for row in session.query(Table).filter(Table.user_id == user_id).all():
            session.delete(row)
            session.commit()
        for row in session.query(Users).filter(Users.user_name == user_name):
            session.delete(row)
            session.commit()
            print('Profile and tasks deleted!')


def update_user(user_id):
    option = input('\n1) Change username\n2) Back\n')
    if option == '1':
        new_name = input('Select new username: ')
        while True:
            if session.query(Users).filter(Users.user_name == new_name).all():
                print('Username already taken!')
                new_name = input('Enter different username: ')
            else:
                break
        session.query(Users).filter(Users.user_id == user_id).update({Users.user_name: new_name})
        session.commit()
        print('Username updated')
    elif option == '2':
        return


def log_out(user_id):
    session.query(Users).filter(Users.user_id == user_id).update({Users.logged_in: 0})
    session.commit()
    print('You\'ve logged out!\n')
    login()


