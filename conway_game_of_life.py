import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use("MacOSX")

# Setting grid size
rows, cols = 50, 50

# Creating grid with dead and alive cells
grid = np.random.choice([0, 1], size=(rows, cols))


# Defining rules
def update(frame, img, grid, rows, cols):
    newGrid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            # Count number of alive neighbors by checking the 8 surrounding cells
            total = int((grid[i, (j - 1) % cols] + grid[i, (j + 1) % cols] +
                         grid[(i - 1) % rows, j] + grid[(i + 1) % rows, j] +
                         grid[(i - 1) % rows, (j - 1) % cols] + grid[(i - 1) % rows, (j + 1) % cols] +
                         grid[(i + 1) % rows, (j - 1) % cols] + grid[(i + 1) % rows, (j + 1) % cols]))

            # Applying rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):  # if less than 2 neighbours, or more than 3 --> cell will die
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1

    # Updating the data
    img.set_data(newGrid)
    grid[:] = newGrid
    return img


# Create a figure and axis
fig, axis = plt.subplots()  # draw more than one plot in one figure
img = axis.imshow(grid, interpolation='nearest')  # display data as an image
animation = animation.FuncAnimation(fig, update, frames=10, fargs=(img, grid, rows, cols), interval=50)

plt.show()
