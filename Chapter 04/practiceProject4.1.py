spam = [2, 'apples', 'bananas', 'tofu', 'cats', 1, 5]

def list_to_string(x):
    name = ''
    for i in range(len(x)):
        if i < int(len(x) - 2):
            name += str(x[i]) + ', '
        elif i < int(len(x) - 1):
            name += str(x[i])
        else:
            name += ' and ' + str(x[i])
    print(name)

list_to_string(spam)
