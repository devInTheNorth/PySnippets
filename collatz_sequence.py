
def collatz(number):
    ''' returns a given number if it is equal to 1, half of
     the number of it is even, (3 * number + 1) if the number is odd but not one '''
    if number == 1:
        print(number)
        return number
    if number % 2 == 0:
        out = int(number/2)
        if out != 1:
            print( out)
            collatz(out)
        else:
            collatz(out)
    else:
        out = int(3 * number + 1)
        if out != 1:
            print(out)
            collatz(out)
        else:
            collatz(out)

def welcomeMsg():
    print('COLLATZ SEQUENCE BY devInTheNorth')
    print('')
    number = int(input("Enter a number "))
    collatz(number)

welcomeMsg()