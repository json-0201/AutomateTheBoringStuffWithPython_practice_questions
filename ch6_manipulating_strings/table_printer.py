def printTable(lists):
    
    # Print the input list of inner lists into a table
    max_width = []

    # Append maximum width of each column
    for ls in lists:
        num = 0
        for item in ls:
            num = max(len(item), num)
        max_width.append(num)
    
    # i -> number of elements in inner lists
    # j -> number of inner lists / columns
    for i in range(len(lists[0])):
        for j in range(len(lists)):
            print(lists[j][i].rjust(max_width[j]), end=" ")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)