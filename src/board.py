#2048 in Python
#pyprocessing for the gui rendering
#Source code in JS: https://github.com/gabrielecirulli/2048
import random
#encode the board state
  #Could do lists of lists (need a multidimensional 4x4 array)
class Board(object):

  def start(self):
    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for t in xrange(1):
      val = getRandomValue()
      pos = self.getRandomPosition() #you already know that the value chosen is unoccupied
      self.addTile(pos, val)

  def addTile(self, val, pos):
    #pos tuple extraction
    x, y = pos
    self.grid[x][y] = val

  def getRandomValue():
    
    
  def getRandomPosition():

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

