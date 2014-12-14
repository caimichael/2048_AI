import random

class AI_Framework(object):
    def makeNextMove(self, game): # accepts the board
        next_move = self.getNextMove(game)
# do something
        next_move = random.randint() % 4
        if next_move == 0:
            game.moveUp()
        elif next_move == 1:
            game.moveRight()
        elif next_move == 2:
            game.moveLeft()
        else
            game.moveDown()

class DFS_AI(AI_Framework):

#Consider what factors determine how "good" a board is to define a heuristic for navigation
#(Will have to be some kind of number so you can compare the values when traversing the tree)
#(This could literally be like the value of the biggest tile)
#to determine how the AI should make a choice
    def getNextMove(self, game):



ai = DFS_AI()
ai.makeNextMove(game)

