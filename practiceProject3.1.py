def main():
    print('Please enter a number:')
    number = int(input())
    
    def collatz(number):
        if number % 2 == 1:
            print(3 * number + 1)
        else:
            print(number // 2)
    collatz(number)


while True:
    try:
        main()
    except ValueError:
        print('Please enter an integer:')
