#2048 in Python
#pyprocessing for the gui rendering
#Source code in JS: https://github.com/gabrielecirulli/2048
import random
#encode the board state
  #Could do lists of lists (need a multidimensional 4x4 array)

def addTile(func):
    def wrapper(*args, **kwargs):
        self = args[0] #because the first argument is the self from the Board object
        func(self)
        self.addRandomTile()
        self.time_step += 1
    return wrapper

class Board(object):

  def __init__(self):
    self.time_step = 0
    self.rvals = []
    self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for tile in xrange(2):
      self.addRandomTile()
      self.time_step += 1


  def pretty_print(self):
      for row in self.grid:
          for cell in row:
              print str(cell) + " ",
          print ""

  def start_text_interface(self):
      input = ""
      while (input != "stop"):
          self.pretty_print()
          input = raw_input()
          if input == "up":
              self.moveUp()
          elif input == "down":
              self.moveDown()
# etc


  def try_move(self, grid, time_step, next_move):
      backed_up_grid = self.grid
      backed_up_time = self.time_step

      self.grid = grid
      self.time_step = time_step

      if next_move == 0:
          self.moveUp()
      elif next_move == 1:
          self.moveRight()
      elif next_move == 2:
          self.moveLeft()
      else:
          self.moveDown()

      resulting_grid = self.grid
      self.grid = backed_up_grid
      self.time_step = backed_up_time

      return resulting_grid

  #This function is for getting the Random value at a specifically queried time
  def getRValAt(self, queried_time):
      if len(self.rvals) > queried_time:
          return self.rvals[queried_time]
      else:
          while not len(self.rvals) > queried_time:
            self.rvals.append(random.random())
          return self.rvals[queried_time]

  def getRandomValue(self):
    if self.getRValAt(self.time_step) > .1:
      return 2
    else:
      return 4

  # picks the random element from choices_list corresponding
  # to the random number chosen at the current time step
  # In this particular case, choice_list is referring to unoccupied_spaces when referring to getRandomPosition
  # Mirroring random.choice, added to the fact that we are choosing from a pre-computed random value
  def choice(self, choice_list):
    random_val = self.getRValAt(self.time_step) - 0.00001 # avoid out of bounds
    chosen_index = int(random_val * len(choice_list))
    return choice_list[chosen_index]

  def getRandomPosition(self):
    unoccupied_spaces = []
    for x, row in enumerate(self.grid):
      for y, val in enumerate(row):
        if val == 0:
          unoccupied_spaces.append((x,y))
    return self.choice(unoccupied_spaces)

  def addRandomTile(self):
    val = self.getRandomValue()
    pos = self.getRandomPosition() #you already know that the value chosen is unoccupied
    x, y = pos
    self.grid[x][y] = val

  def addSpecificTile(self, pos, val):
    x, y = pos
    self.grid[x][y] = val

  @addTile
  def moveRight(self):
    #Have to move right, passing unoccupied spaces until it hits the end of the grid,
    #or hits a number that is different than the moving tile and stops
    #If the tile it collides with is the same, then sum the values/collapse the tile
    for row in xrange(4):
      for start_tile in xrange(2, -1): #i is the location of the tile when we found it
        if self.grid[row][start_tile] != 0:
          current_tile = start_tile #j is the location of the tile as we're processing it/right now
          while current_tile != 3 and self.grid[row][current_tile+1] == 0:
            self.grid[row][current_tile+1] = self.grid[row][current_tile]
            self.grid[row][current_tile] = 0
            current_tile += 1
          if current_tile < 3 and self.grid[row][current_tile+1] == self.grid[row][current_tile]:
            self.grid[row][current_tile+1] *= 2
            self.grid[row][current_tile] = 0
          else:
            continue

#  @addTile
#  def moveLeft(self):
#    #workon own

  @addTile
  def moveUp(self):
    for col in xrange(4):
      for start_tile in xrange(1,4):
        if self.grid[start_tile][col] != 0:
          current_tile = start_tile
          while current_tile != 0 and self.grid[current_tile-1][col] == 0:
            self.grid[current_tile-1][col] = self.grid[current_tile][col]
            self.grid[current_tile][col] = 0
            current_tile -= 1
          if current_tile > 0 and self.grid[current_tile-1][col] == self.grid[current_tile][col]:
            self.grid[current_tile-1][col] *=2
            self.grid[current_tile][col] = 0
          else:
            continue

#  @addTile
#  def moveDown(self):
#    #workon own

#start

#handle the functions of adding a new random tile
#move the tile
  #handle the shifts
  #handle the combinations

#have the current state of the board be a class
  #the functions that change the game state, return a new class with a new game state in it
  #starting node is the current game state
    #four children are the four different new game states
    #each increment down 1 depth is a new four game states per branch

#Have the AI know the outcome of a choice beforehand so that the complexity is reduced
#To the observer, it will not look odd since it is a valid traversal of a real 2048 game
#But the AI will just know what each choice's outcome [the random value that comes in] will be

