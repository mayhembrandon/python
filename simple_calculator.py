#Simple calculator programmed by Python working as of 09.12.2020
#Made by Mayhem Brandon xD
while True:
    print('Whats the weather like?')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Remainder')
    print('6. Exit')

    def add(x,y):
        return x + y
    def sub(x,y):
        return x - y
    def mul(x,y):
        return x * y
    def div(x,y):
        return x / y
    def rem(x,y):
        return x % y

    schoice = (input("Make a selection... Or maybe take a nap...xD  "))

    try:
        choice = int(schoice)

#if alphabetic characters were inputted
    except:
        print('Input only values between 1-6!')
        print()
        continue

    if (choice>=1 and choice<=5):
            print('Input two values')
            num1 = int(input('1st value..'))
            num2 = int(input('2nd value..'))

    if choice == 1:

            add(num1,num2)
            print(num1,'+',num2,'=',add(num1,num2))
            print()

    elif choice == 2:

            sub(num1,num2)
            print(num1,'-',num2,'=',sub(num1,num2))
            print()

    elif choice == 3:

            mul(num1,num2)
            print(num1,'*',num2,'=',mul(num1,num2))
            print()

    elif choice == 4:

            div(num1,num2)
            print(num1,'/',num2,'=',div(num1,num2))
            print()

    elif choice == 5:

            rem(num1,num2)
            print(num1,'%',num2,'=',rem(num1,num2))
            print()

    elif choice == 6:

            print('Good riddance!')
            break

#if any integers between 1-6 are not inputted
    else:
            print('Try again with an integer between 1-6')
            print()
            continue
