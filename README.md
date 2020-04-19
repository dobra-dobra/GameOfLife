# Python3 / tkinter implementation of the Conway's Game Of Life
by Szymon Jakubiak

Tested in Python 3.2.3 and Python 3.8.2

## Configuration

It is possible to configure the following simulation parameters by editing constants near the top of the GameOfLife.py file:
* size of the game window is determined by the number of cells horizontally (WORLD_WIDTH) and vertically (WORLD_HEIGHT) as well as the size of a single cell in pixels (CELL_SIZE)
* behavior of the cells at the edge of the screen: if ROUND_WORLD has value True cells from first column / row will interact with cells from last column / row; if ROUND_WORLD has value False edge of the screen is recognized as a dead cell
* if USE_USER_SEED has value True USER_SEED will be used to seed the world with live cells at the beginning of the simulation; USE_USER_SEED has value False random seed will be generated and printed into serial console
* fraction of the screen seeded at the beginning of the simulation is defined by SIZE_OF_INITIAL_COLONY
* BACKGROUND_COLOUR and LIVE_CELL_COLOUR can be used to define background and live cell colour in HTML format; at the time of writing red and blue channels are switched in case of the PewPew M4
* UPDATE_DELAY can be used to slow down the simulation, it's the sleep time in seconds between the consecutive state calculations
