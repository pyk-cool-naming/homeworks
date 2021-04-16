try:
    firstch = int(input(':'))
    secondch = int(input(':'))
    act = input(':')
except ValueError:
    print('must be integer!')
except ZeroDivisionError:
    print('you can`t divide on zero')
else:
    if act == '/':
        print(firstch / secondch)
    elif act == '+':
        print(firstch + secondch)
    elif act == '-':
        print(firstch - secondch)
    elif act == '*':
        print(firstch * secondch)