# Python3 / tkinter implementation of Conway's Game Of Life
by Szymon Jakubiak

Tested in Python 3.2.3

## Configuration

It is possible to configure following simulation parameters by editing
constants in the header of GameOfLife.py file:
* size of the game window is determined by the number of cells
diagonally (WORLD_WIDTH) and vertically (WORLD_HEIGHT) as well as the size
of a single cell in pixels (CELL_SIZE)
* behavior of cells at window boarder: if ROUND_WORLD has value True cells
from first column / row will interact with cells from last column / row,
what for example allows ship to fly around the world; if ROUND_WORLD has value
False boarder of the screen is recognized as a dead cell

## Future plans and ideas

* implement mechanism to measure time
* display used seed and other simulation options in main window
* implement possibility of external hardware use to display cells
* end simulation or just note the year when there was no evolution in recent years
* implement system to recognize created structures and save year of observation
