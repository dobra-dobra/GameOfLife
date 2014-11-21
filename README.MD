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
False boarder of the screen is counted as a dead cell

## Future plans and ideas

* implement years, centuries and milleniums to measure time
* display current date (elapsed time) in main window
* display used seed and other simulation options in main window
* end simulation when there was no change in last year
* implement system to recognize created structures and save year of observation
