
from arcade.sprite_list.sprite_list import SpriteList
import GamePiece as gp
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
        self.blocks = [[None for y in range(width)] for x in range(height)]
        self.playerSprites = SpriteList()
        self.groundSprites = SpriteList()


    def draw(self):
        self.playerSprites.draw()
        self.groundSprites.draw()

    def canMoveBlock(self, x: int, y: int) -> bool:
        return self.blocks[x][y] is None

    def canMoveGamePiece(self, gamePiece:gp.GamePiece, x:int, y:int) -> bool:
        pass

    def addBlock(self, block: gp.Block):
        """adds block to the game board"""

        if self.blocks[block.x][block.y] != None:
            raise MovementError('game board space not empty')
        self.blocks[block.x][block.y] = block
        self.groundSprites.append(block.sprite)

    def addGamePiece(self, gamePiece:gp.GamePiece):
        for block in gamePiece.allBlocks():
            if block is None:
                continue
            self.blocks[block.x][block.y] = block
            self.playerSprites.append(block.sprite)

    def moveBlock(self, block: gp.Block, x: int, y: int):
        self.removeBlock(block)
        self.blocks[x][y] = block

    def removeBlock(self, block: gp.Block):
        """ remove a block from the game board """
        if (self.blocks[block.x][block.y] is not block):
            raise MovementError('block not found on game board')
        self.blocks[block.x][block.y] = None

class GameManager:

    def __init__(self) -> None:
        pass
    
    def start(self):
        gameBoard = GameBoard(10, 20)
        gameBoard.addGamePiece()