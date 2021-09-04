
from arcade.sprite_list.sprite_list import SpriteList
import GamePiece as gp
import numpy as np
from Errors import *

class GameConfig:
    WINDOW_TITLE = "MyPyTris"
    SCREEN_WIDTH = 450
    SCREEN_HEIGHT = 900
    BLOCK_PX = 45 # 45px blocks on screen
    SPRITE_PX = 64 # 64px sprite
    BLOCK_SCALE = BLOCK_PX/SPRITE_PX # sprite scale ratio

class GameBoard:
    """ Class to manage blocks on the game board """

    def __init__(self, width: int, height: int):
        # 2D list of blocks initialized to empty in the width and height of our game board
        self.width = width
        self.height = height
        self.blocks = np.array([[None for y in range(width)] for x in range(height)], dtype=gp.Block)
        self.playerPiece:gp.GamePiece = None
        self.playerSprites = SpriteList()
        self.groundSprites = SpriteList()


    def draw(self):
        self.playerSprites.draw()
        self.groundSprites.draw()

    def canMoveBlock(self, x: int, y: int) -> bool:
        return self.blocks[x][y] is None

    def canMoveGamePiece(self, pieceMask:np.ndarray, gamePiece:gp.GamePiece, xTo:int, yTo:int) -> bool:
        for point, value in np.ndenumerate(pieceMask):
            if value == 0:
                continue
            newX = xTo + point[1]
            newY = yTo + point[0]
            if newX >= self.width or newX < 0:
                return False
            if newY < 0 or newY >= self.height:
                return False
            if self.blocks[newY][newX] is not None \
                and self.blocks[newY][newX] not in gamePiece.allBlocks():
                return False
        return True

    def rotateGamePiece(self, gamePiece:gp.GamePiece):
        # check if we can rotate 90 degrees
        if not self.canMoveGamePiece(np.rot90(gamePiece.getMask()), gamePiece, gamePiece.x, gamePiece.y):
            return # nope, bail out

        # rotate 90 degrees
        gamePiece.blocks = np.rot90(gamePiece.blocks)
        for y, row in enumerate(gamePiece.blocks):
            for x, block in enumerate(row):
                if block is None:
                    continue
                block.moveTo(gamePiece.x + x, gamePiece.y + y)
        gamePiece.rotation = gamePiece.rotation + 1 % 3
        
    def moveGamePiece(self, gamePiece:gp.GamePiece, xTo:int, yTo:int):
        if (not self.canMoveGamePiece(gamePiece.getMask(), gamePiece, xTo, yTo)):
            return False

        # remove blocks from game board
        for y, row in enumerate(gamePiece.blocks):
            for x, block in enumerate(row):
                if block is not None:
                    self.blocks[y + gamePiece.y][x + gamePiece.x] = None

        # add blocks in new positions
        for y, row in enumerate(gamePiece.blocks):
            for x, block in enumerate(row):
                if block is not None:
                    blockXDiff = block.x - gamePiece.x
                    blockYDiff = block.y - gamePiece.y
                    newBlockX = xTo + blockXDiff
                    newBlockY = yTo + blockYDiff
                    self.blocks[newBlockY][newBlockX] = block
                    block.moveTo(newBlockX, newBlockY)

        gamePiece.x = xTo
        gamePiece.y = yTo
        

    def addBlock(self, aBlock: gp.Block):
        """adds a block to the game board"""

        if self.blocks[aBlock.y][aBlock.x] != None:
            raise MovementError('game board space not empty')
        self.blocks[aBlock.y][aBlock.x] = aBlock
        self.groundSprites.append(aBlock.sprite)

    def addPlayerPiece(self, gamePiece:gp.GamePiece):
        for y in range(gamePiece.size):
            for x in range(gamePiece.size):
                block = gamePiece.blocks[y][x]
                if block is None:
                    continue
                self.blocks[block.y][block.x] = block
                self.playerSprites.append(block.sprite)
        self.playerPiece = gamePiece

    def moveBlock(self, aBlock: gp.Block, x: int, y: int):
        self.blocks[aBlock.y][aBlock.x] = None
        self.blocks[y][x] = aBlock

    def removeBlock(self, aBlock: gp.Block):
        """ remove a block from the game board """
        
        for y, row in enumerate(self.blocks):
            for x, block in enumerate(row):
                if block is aBlock:
                    self.blocks[y][x] = None
                    self.playerSprites.remove(aBlock.sprite)
                    return

class GameEngine:
    """Class to manage falling pieces and line detection"""

    def __init__(self, gameBoard:GameBoard) -> None:
        self.board = gameBoard
        self.speed = 1.
        self.deltaSinceLastMove = 0.

    def on_update(self, deltaTime:float):
        self.deltaSinceLastMove + deltaTime
        if self.deltaSinceLastMove > self.speed:
            self.doPlayerGravity()

    def doPlayerGravity(self):
        self.board.playerPiece