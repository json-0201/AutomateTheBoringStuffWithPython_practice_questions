# Copy the previous grid value, and write code that uses it to print the image:
#   ..OO.OO..
#   .OOOOOOO.
#   .OOOOOOO.
#   ..OOOOO..
#   ...OOO...
#   ....O....

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end="")
    print()