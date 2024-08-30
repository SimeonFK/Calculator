
def main(current_problem):
    result = 0
    num1 = float(current_problem[0])
    operator = current_problem[1]
    num2 = float(current_problem[2])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
         result = num1 / num2
    else:
        print('Invalid operator! Try again!')
    return result


def problem():
    print('Type your problem bellow:')
    action = input().split()
    solving = main(action)
    return solving


def continuing():
    continue_forward = input('Would you like to continue with the problem{a},\ncontinue with a new one{c}, if type in a operator, exit or start: ')
    return continue_forward


current_result = 0
while True:
    action = continuing()
    c = action[0]
    if c.lower() == 'e':
        break
    elif c.lower() == 's':
        p = problem()
        current_result += p
    elif c == 'a':
        p = problem()
        o = action[1]
        if o == '+':
            current_result += p
        elif o == '-':
            current_result -= p
        elif o == '*':
            current_result *= p
        elif o == '/':
            current_result /= p

    elif c == 'c':
        p = problem()
        current_result = 0
        current_result += p
        o = action[1]
        if o == '+':
            current_result += p
        elif o == '-':
            current_result -= p
        elif o == '*':
            current_result *= p
        elif o == '/':
            current_result /= p

print("Here is your final result:")
print(current_result)
