tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'David', 'Carol'],
             ['dogs', 'cats', 'moose', 'goose']] 

def printTable(table):
    colWidth = [0] * len(table)
    
    count = 0 
    while count < len(table):
        for item in table[count]:
            if len(item) > colWidth[count]:
                colWidth[count] = len(item)
        count += 1

    for category in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][category].rjust(colWidth[item]), end =' ')
            print()
printTable(tableData)
