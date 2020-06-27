import random
import sqlite3
conn = sqlite3.connect('card.s3db')
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS card(
                    id INT,
                    number TEXT,
                    pin TEXT,
                    balance INTEGER DEFAULT 0);""")


def create_entry(account_id, card_number, pin):
    c.execute("INSERT INTO card(id, number, pin) values(?, ?, ?)", (account_id, card_number, pin))
    conn.commit()


def menu_1():
    while True:
        print("""1. Create an account
2. Log into account
0. Exit""")
        option = input()
        if option == '1':
            create_pin()
        elif option == '2':
            card_number = input('\nEnter your card number:\n')
            pin_number = input('Enter you PIN:\n')
            log_in(card_number, pin_number)
        else:
            print('\nBye')
            exit()


def create_account(pin):
    number_list = []
    double = []
    bin = '400000'  # bank id number
    account_id = str(format(random.randrange(1000000000), '09d'))
    number = bin + account_id
    for num in number:
        number_list.append(num)
    for i in range(0, 15):
        if i % 2 == 0:
            double.append(str(int(number_list[i]) * 2))
        else:
            double.append(number_list[i])
    for n in range(0, 15):
        if int(double[n]) > 9:
            sub = int(double[n]) - 9
            double[n] = int(sub)
        else:
            double[n] = int(double[n])

    total = sum(double)
    if total % 10 == 0:
        check_sum = 0
    else:
        check_sum = ((total // 10 + 1) * 10 - total)
    card_number = number + str(check_sum)
    create_entry(account_id, card_number, pin)
    print(f"""\nYour card has been created
Your card number:\n{card_number}""")


def create_pin():
    digit_1 = (random.randrange(10))
    digit_2 = (random.randrange(10))
    digit_3 = (random.randrange(10))
    digit_4 = (random.randrange(10))
    pin = f'{digit_1}{digit_2}{digit_3}{digit_4}'
    create_account(pin)
    print(f'Your card PIN:\n{pin}\n')


def is_valid(transfer_to, card_num, pin_num):
    number_list = []
    double = []
    for num in transfer_to:
        number_list.append(num)
    for i in range(0, 15):
        if i % 2 == 0:
            double.append(str(int(number_list[i]) * 2))
        else:
            double.append(number_list[i])
    for n in range(0,15):
        if int(double[n]) > 9:
            sub = int(double[n]) - 9
            double[n] = int(sub)
        else:
            double[n] = int(double[n])
    total = sum(double) + int(number_list[15])
    if total % 10 == 0:
        check_num(transfer_to, card_num, pin_num)
    else:
        print('You have probably made a mistake in the card number. Please try again!\n')
        menu_2(card_num, pin_num)


def check_num(transfer_to, card_num, pin_num):
    transfer = c.execute("SELECT balance FROM card WHERE number = ?", (transfer_to,))
    if not transfer.fetchone():
        print('Such a card does not exist.\n')
        menu_2(card_num, pin_num)


def log_in(card_num, pin_num):
    account = c.execute("SELECT id, number, pin, balance FROM card WHERE number =? AND pin = ?", (card_num, pin_num,))
    if account.fetchone():
        print('\nYou have successfully logged in!\n')
        menu_2(card_num, pin_num)
    else:
        print('\nWrong card or PIN\n')


def menu_2(card_num, pin_num):
    while True:
        print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
        option = input()
        if option == '1':
            balance = c.execute("SELECT balance FROM card WHERE number = ? AND pin = ?", (card_num, pin_num,))
            for rows in balance:
                print('\nBalance: ' + str(rows[0]) + '\n')
        elif option == '2':
                income = input('\nEnter income: \n')
                add_income(income, card_num, pin_num)
        elif option == '3':
            transfer_to = input('\nTransfer\nEnter card number:\n')
            is_valid(transfer_to, card_num, pin_num)
            transfer(transfer_to, card_num)
        elif option == '4':
            close_account(card_num, pin_num)
        elif option == '5':
            print('\nYou have successfully logged out!\n')
            break
        else:
            print('Bye')
            exit()


def add_income(income, card_num, pin_num):
    c.execute("UPDATE card SET balance = balance + ? WHERE number = ? AND pin = ?", (income, card_num, pin_num,))
    conn.commit()
    print('Income was added! \n')


def transfer(tranfer_to, card_num):
    amount = int(input('Enter how much you want to transfer:\n'))
    current_balance = c.execute("SELECT balance FROM card WHERE number = ?", (card_num,))
    if amount > current_balance.fetchone()[0]:
        print('Insufficient funds!\n')
    else:
        c.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, tranfer_to))
        c.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (amount, card_num))
        conn.commit()
        print('Success!\n')


def close_account(card_num, pin_num):
    c.execute("DELETE FROM card WHERE number = ? AND pin = ?", (card_num, pin_num))
    conn.commit()
    print('\n The account has been closed!\n')


create_table()
menu_1()
c.close()
conn.close()

