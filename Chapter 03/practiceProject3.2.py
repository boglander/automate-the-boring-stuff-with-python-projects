
print('Please enter a number:')
number = int(input())

def collatz(number):
    while number != 1:
        if number % 2 == 1:
            print(3 * number + 1)
            number = 3 * number + 1
        else:
            print(number // 2)
            number = number // 2
collatz(number) 

