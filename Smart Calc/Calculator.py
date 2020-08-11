def help_():
    return 'The program calculates the sum and subtraction of numbers.'


def check_sign(signs):
    lst_signs = []
    op_value = 0
    for i in signs:
        if i != '':
            if '*' not in i:
                if len(i) != 1:
                    for j in i:
                        if j == '+':
                            op_value += 1
                        elif j == '-':
                            op_value -= 1
                    if op_value > 0:
                        lst_signs.append('+')
                    else:
                        if op_value == 0:
                            lst_signs.append('-')
                        elif op_value % 2 == 0:
                            lst_signs.append('+')
                        else:
                            lst_signs.append('-')
                    op_value = 0
                else:
                    lst_signs.append(i)
            else:
                lst_signs.append(i)
    return lst_signs


def var_name_check(var_name):
    numeric = 0
    for i in var_name:
        if i.isnumeric():
            numeric += 1
    if numeric > 0:
        return False
    else:
        return True


def value_check(var_value):
    if var_value in variables:
        return True
    else:
        return False


def value_assignment(value):
    for i in value:
        if i.isnumeric():
            try:
                if value[(value.index(i) + 1)].isnumeric():
                    return True
            except IndexError:
                return True
            else:
                return False
        elif i.isalpha():
            try:
                if value[(value.index(i) + 1)].isalpha():
                    return True
            except IndexError:
                return True
            else:
                return False


def main():
    var = nums.replace(' ', '').split('=')
    if len(var) <= 2:
        if '+' not in nums:
            if '-' not in nums:
                if '*' not in nums:
                    if '/' not in nums:
                        if var_name_check(var[0]):
                            try:
                                if value_assignment(var[1]):
                                    if var[0] in variables:
                                        if len(var) == 1:
                                            print(variables[var[0]])
                                        elif variables[var[0]] != var[1]:
                                            if var[1].isalpha():
                                                if var[1] not in variables:
                                                    print('Unknown variable')
                                                else:
                                                    variables.update({var[0]: variables[var[1]]})
                                            else:
                                                variables.update({var[0]: var[1]})
                                    else:
                                        try:
                                            if value_check(var[1]):
                                                variables[var[0]] = variables[var[1]]
                                            elif not value_check(var[1]):
                                                if not var[1].isnumeric():
                                                    print('Unknown variable')
                                                else:
                                                    variables[var[0]] = var[1]
                                        except IndexError:
                                            print('Unknown variable')
                                else:
                                    print('Invalid assignment')
                            except IndexError:
                                if var[0] in variables:
                                    print(variables[var[0]])
                                else:
                                    print('Unknown variable')
                        else:
                            print('Invalid identifier')
                    else:
                        new_eq = []
                        for i in var[0]:
                            if i in variables:
                                new_eq.append(variables[i])
                            else:
                                new_eq.append(i)
                        print(calc(''.join(new_eq)))
                else:
                    new_eq = []
                    for i in var[0]:
                        if i in variables:
                            new_eq.append(variables[i])
                        else:
                            new_eq.append(i)
                    print(calc(''.join(new_eq)))
            else:
                new_eq = []
                for i in var[0]:
                    if i in variables:
                        new_eq.append(variables[i])
                    else:
                        new_eq.append(i)
                print(calc(''.join(new_eq)))
        else:
            new_eq = []
            for i in var[0]:
                if i in variables:
                    new_eq.append(variables[i])
                else:
                    new_eq.append(i)
            print(calc(''.join(new_eq)))
    else:
        print('Invalid assignment')


def calc(final):
    try:
        return int(eval(final))
    except SyntaxError:
        return 'Invalid expression'


if __name__ == '__main__':
    global signs
    global eq
    abc = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    variables = {}
    while True:
        count = 0
        nums = input().lstrip()
        if not nums.startswith('/'):
            if count % 2 == 0:
                if nums != '':
                    if nums[0] not in abc:
                        if '+' in nums or '-' in nums or '/' in nums or '*' in nums:
                            slashes = 0
                            for i in nums:
                                if i == '/':
                                    slashes += 1
                            if slashes > 1:
                                print('Invalid expression')
                            else:
                                main()
                        else:
                            if ' ' not in nums:
                                print(nums)
                            else:
                                print('Invalid expression')
                    else:
                        main()
            else:
                print('Invalid expression')
        else:
            if nums == '/exit':
                print('Bye!')
                break
            elif nums == '/help':
                print(help_())
            else:
                print('Unknown command')

