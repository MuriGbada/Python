print('You are welcome, please input your pin number')
true = True
while true:
    pin = input('enter you pin\n')
    if len(pin) > 4:
        print('pin must be four characters')
    elif len(pin) < 4:
        print('pin should be at least four characters')
    else:
        transaction = input('withdrawal, checkbalance, transfer, open account')
        if transaction == 'withdrawal':
            choice = input('saving, current\n')
            if choice == 'saving':
                pin = input('enter your pin\n')
                if len(pin) > 4:
                    print('pin must be four characters')
                elif len(pin) < 4:
                    print('pin should be at least four characters')
                else:
                    input('enter your amount #')
                    print('take your cash...')
                    print('THANKS FOR YOUR PATRONAGE')
                    true = False
                    break
            elif choice == 'current':
                pin = input('enter your pin')
                if len(pin) > 4:
                    print('pin must be four characters')
                elif len(pin) < 4:
                    print('pin should be at least four characters')
                else:
                    input('enter your amount "#')
                    print('take your cash...')
                    print('THANK FOR PATRONAGE')
                    true = False
                    break
        if transaction == 'checkbalance':
            print('checking.. ')
            print('your balance is ...')
            true = False
            break
        if transaction == 'transfer':
            input('enter account number')
            bank = input('enter bank name')
            print('you are welcome to ',bank)
            input('enter amount "#')
            print('transfering...')
            print('please wait')
            print('Approved')
            true = False
            break
        if transaction == 'open account':
            name1 = input('first name')
            name2 = input('middle name')
            name3 = input('last name')
            int(input('enter your BVN number'))
            code = (input('enter your account code'))
            if len(code) > 4:
                print('too long')
            elif len(code) < 4:
                print(' too short')
                true = False
            else:
                answer = input('do you wish to proceed?')
                if answer == 'yes' or 'yeah':
                    print(f'{name1}{name2}{name3} you have successfully open an account')
                    print('THANKS FOR YOUR PATRONAGE')