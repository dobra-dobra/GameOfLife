######################################################################
# Game of life                                                       #
#                                                                    #
# Code by Szymon Jakubiak                                            #
#                                                                    #
# Tested in Python 3.2.3                                             #
######################################################################

from tkinter import *
from tkinter import messagebox
import random

# Options
WORLD_WIDTH = 100   # number of cells horizontally
WORLD_HEIGHT = 80   # number of cells vertically
CELL_SIZE = 8   # size of a cell in pixels
ROUND_WORLD = True   # if True object can move around the edges, if False edge is treated as an empty cell
USE_USER_SEED = False   # if True USER_SEED will be used to settle cells on world map at the beginning, if False random seed will be generated
USER_SEED = '065992'   # seed for initial colony of cells (string with six digits)
DRAW_GRID = False   # if True world will be divided into cells
GRID_COLOUR = 'black'
BACKGROUND_COLOUR = 'white'
LIVE_CELL_COLOUR = 'orange'
SIZE_OF_INITIAL_COLONY = 0.5   # fraction of the world seeded with cells at the beginning of the simulation
YEAR_LENGTH = 100   # time in ms before changing state of the colony (it may take longer depending on total number of cells)

# Constants
VERSION = '0.33'
CENTER_X = int(WORLD_WIDTH / 2)
CENTER_Y = int(WORLD_HEIGHT / 2)
WINDOW_WIDTH = WORLD_WIDTH * CELL_SIZE
WINDOW_HEIGHT = WORLD_HEIGHT * CELL_SIZE

# Variables
cells = []   # array where Cell objects will be stored

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.live = False

    def change_state(self):   # changes state of the cell to opposite
        self.live = not self.live
        if self.live:
                top_left_x = self.x * CELL_SIZE
                top_left_y = self.y * CELL_SIZE
                self.representation = canvas.create_rectangle(top_left_x, top_left_y,
                                                         top_left_x + CELL_SIZE, top_left_y + CELL_SIZE,
                                                         fill = LIVE_CELL_COLOUR)
        else:
            canvas.delete(self.representation)

    def check_neighbours(self):
        self.live_neighbours = 0
        x_to_check = [self.x]
        y_to_check = [self.y]
        if ROUND_WORLD:
            y_to_check.append((self.y - 1) % WORLD_HEIGHT)
            y_to_check.append((self.y + 1) % WORLD_HEIGHT)
            x_to_check.append((self.x - 1) % WORLD_WIDTH)
            x_to_check.append((self.x + 1) % WORLD_WIDTH)
        else:
            if self.y > 0:   # if cell is in row 0 it doesn't have neighbours above
                y_to_check.append(self.y - 1)
            if self.y < WORLD_HEIGHT - 1:   # if cell is in the lowest row it doesn't have neighbours below
                y_to_check.append(self.y + 1)
            if self.x > 0:   # if cell is in left column it doesn't have neighbours from left side
                x_to_check.append(self.x - 1)
            if self.x < WORLD_WIDTH - 1:   # if cell is in right column it doesn't have neighbours from right side
                x_to_check.append(self.x + 1)
        for y in y_to_check:
            for x in x_to_check:
                if y != self.y or x != self.x:
                    if cells[x][y].live == True:
                        self.live_neighbours += 1

    def check_rules(self):
        if self.live == True:
            if self.live_neighbours < 2 or self.live_neighbours > 3:
                self.change_state()
        if self.live == False and self.live_neighbours == 3:
            self.change_state()

# Helper function used to draw a grid on a world map
def draw_grid():
    for x in range (1, WORLD_WIDTH):
        canvas.create_line(x * CELL_SIZE, 0,
                      x * CELL_SIZE, WINDOW_HEIGHT,
                      fill = GRID_COLOUR)
    for y in range (1, WORLD_HEIGHT):
        canvas.create_line(0, y * CELL_SIZE,
                      WINDOW_WIDTH, y * CELL_SIZE,
                      fill = GRID_COLOUR)

# Create world filled with dead cells
def create_world():
    global cells
    for x in range(0, WORLD_WIDTH):
        cells.append([])
        for y in range(0, WORLD_HEIGHT):
            cells[x].append(Cell(x, y))

# Randomize initial state
def seed_world():
    global cells
    randomized_seed = ''
    if USE_USER_SEED:
        random.seed(USER_SEED)
        print('World seed: ', USER_SEED)
    else:
        for counter in range(0, 6):
            randomized_seed += str(random.randrange(0, 10))
        random.seed(int(randomized_seed))
        print('World seed: ', randomized_seed)
    for y in range(int(CENTER_Y - SIZE_OF_INITIAL_COLONY * CENTER_Y),
                   int(CENTER_Y + SIZE_OF_INITIAL_COLONY * CENTER_Y)):
        for x in range(int(CENTER_X - SIZE_OF_INITIAL_COLONY * CENTER_X),
                       int(CENTER_X + SIZE_OF_INITIAL_COLONY * CENTER_X)):
            finger_of_god = random.randrange(0, 2)
            if finger_of_god == 1:
                cells[x][y].change_state()

# Helper function used to update state of the colony
def update_colony():
    global population_year
    for row in cells:
        for cell in row:
            cell.check_neighbours()
    for row in cells:
        for cell in row:
            cell.check_rules()
    main.after(YEAR_LENGTH, update_colony)

def show_info():
    messagebox.showinfo(title = 'About', message = 'Game of Life ver. ' + VERSION + "\nAuthor: Szymon Jakubiak")

def close_window():
    decision = messagebox.askyesno(title = 'Quit', message = 'Do You want to Quit?')
    if decision == True:
        process_rules = False
        canvas.destroy()
        main.destroy()

main = Tk()
main.title('Game of Life')

menu_bar = Menu(main)
options_menu = Menu(menu_bar, tearoff = 0)
options_menu.add_command(label = 'About', command = show_info)
options_menu.add_command(label = 'Quit', command = close_window)
menu_bar.add_cascade(label = 'Options', menu = options_menu)
main.config(menu = menu_bar)

canvas = Canvas(main,
           width = WINDOW_WIDTH,
           height = WINDOW_HEIGHT,
           bg = BACKGROUND_COLOUR)
canvas.pack()

if DRAW_GRID:
        draw_grid()
create_world()
seed_world()
main.after(YEAR_LENGTH, update_colony)
main.mainloop()

