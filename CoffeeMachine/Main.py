def menu():
    return input('Write action (buy, fill, take, remaining, exit):\n')


def machine_stock(stock, action):
    print(f"""\nThe coffee machine has:
{stock['water']} of water
{stock['milk']} of milk
{stock['beans']} of coffee beans
{stock['cups']} of disposable cups
{stock['money']} of money\n""")
    if action.lower() == 'fill':
        fill(stock)
    elif action.lower() == 'buy':
        buy(stock)
    elif action.lower() == 'take':
        take(stock)
    elif action.lower() == 'exit':
        return True


def buy(stock):
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}
    option = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
    if option == '1':
        coffee(espresso, stock)
    elif option == '2':
        coffee(latte, stock)
    elif option == '3':
        coffee(cappuccino, stock)


def fill(stock):
    print('\n')
    stock['water'] += int(input('Write how many ml of water do you want to add:\n'))
    stock['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
    stock['beans'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
    stock['cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    print('\n')


def take(stock):
    print(f"I gave you ${stock['money']}\n")
    stock['money'] = 0

def coffee(type, stock):
    num_cups = 1
    vol_water = num_cups * type['water']
    vol_milk = num_cups * type['milk']
    vol_beans = num_cups * type['beans']
    if stock['water'] > vol_water:
        if stock['milk'] > vol_milk:
            if stock['beans'] > vol_beans:
                if stock['cups'] > num_cups:
                    print('I have enough resources, making you a coffee!\n')
                    stock['water'] -= vol_water
                    stock['milk'] -= vol_milk
                    stock['beans'] -= vol_beans
                    stock['money'] += type['cost']
                    stock['cups'] -= num_cups
                else:
                    print('Sorry, not enough cups!\n')
            else:
                print('Sorry, not enough beans!\n')
        else:
            print('Sorry, not enough milk!\n')
    else:
        print('Sorry, not enough water!\n')


stock = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
while True:
    action = menu()
    if action == 'buy':
        buy(stock)
    elif action == 'fill':
        fill(stock)
    elif action == 'take':
        take(stock)
    elif action == 'remaining':
        machine_stock(stock, action)
    elif action == 'exit':
        break



