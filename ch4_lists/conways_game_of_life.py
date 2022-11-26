# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []  # Initial cells -> Updated when while loop begins
for x in range(WIDTH):
    column = [] # Create a new column

    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Add a living cell
        else:
            column.append(" ") # Add a dead cell
    
    nextCells.append(column)    #nextCells is a list of column lists


while True: # Main program loop
    print("\n\n\n\n\n") # Separate each step with newlines
    currentCells = copy.deepcopy(nextCells) # deepcopy -> copy lists in the main list
                                            # decoy cells for processing

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")   # Print the # or space
        print() # Print a newline at the end of the row
    
    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # "% WIDTH" ensures leftCoord is always between 0 and WIDTH - 1
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            up = (y - 1) % HEIGHT
            down = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[left][up] == "#":
                numNeighbors += 1   # Top-left neighbor is alive
            if currentCells[x][up] == "#":
                numNeighbors += 1   # Top neighbor is alive
            if currentCells[right][up] == "#":
                numNeighbors += 1   # Top-right neighbor is alive
            if currentCells[left][y] == "#":
                numNeighbors += 1   # Left neighbor is alive
            if currentCells[right][y] == "#":
                numNeighbors += 1   # Right neighbor is alive
            if currentCells[left][down] == "#":
                numNeighbors += 1   # Bottom-left neighbor is alive
            if currentCells[x][down] == "#":
                numNeighbors += 1   # Bottom neighbor is alive
            if currentCells[right][down] == "#":
                numNeighbors += 1   # Bottom-right neighbor is alive

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = "#"

            elif currentCells[x][y] == " " and numNeighbors == 3:
                nextCells[x][y] = "#"

            else:
                nextCells[x][y] = " "
    time.sleep(1)   # Add a 1-second pause to reduce flickering