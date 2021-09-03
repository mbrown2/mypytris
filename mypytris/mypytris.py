""" My PyTris is a tetris style game made with Python Arcade

Its cool because I made it.
"""

from enum import Enum
import arcade
import numpy
from arcade.sprite_list.sprite_list import SpriteList


class GameConfig:
    WINDOW_TITLE = "MyPyTris"
    SCREEN_WIDTH = 450
    SCREEN_HEIGHT = 900
    BLOCK_PX = 45 # 45px blocks on screen
    SPRITE_PX = 64 # 64px sprite
    BLOCK_SCALE = BLOCK_PX/SPRITE_PX # sprite scale ratio

class Block:
    """ Single block class """

    def __init__(self, x:int = 0, y:int = 0, imgPath = r'mypytris/sprites/Blocks_01_64x64_Alt_00_001.png'):
        self.sprite = arcade.Sprite(imgPath, GameConfig.BLOCK_SCALE)
        self.moveTo(x, y)

    def moveTo(self, x:int, y:int) -> None:
        # scale position from block grid to screen pixels
        self.sprite.left = x * GameConfig.BLOCK_PX
        self.sprite.bottom = y * GameConfig.BLOCK_PX
        self.x = x
        self.y = y

class GamePieceConfig:

    def __init__(self, imgPath:str, shape:list[list[int]]) -> None:
        self.shape = shape
        self.imgPath = imgPath
GamePieceConfig.SQUARE = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_004.png', 
                                         [[1,1],
                                          [1,1]])
GamePieceConfig.T = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_003.png', 
                                    [[0,0,0],
                                     [0,1,0],
                                     [1,1,1]])

class GamePiece:
    """ Game pieces are composed of multiple blocks that form a game piece shape """

    def __init__(self, config:GamePieceConfig):
        self.config = config
        self.size = len(self.config.shape)
        self.blocks = [[] for y in range(self.size)]
        for y in range(self.size):
            self.blocks.append([])
            for x in range(self.size):
                self.blocks[y].append(Block(x, y, config.imgPath) if self.config.shape[y][x] == 1 else None)

        #self.blocks = [[Block(x,y, self.config.imgPath) for y in reversed(range(self.size)) if self.config.shape[x][y] == 1] for x in range(self.size)]
        self.x = 0
        self.y = 0

    def moveTo(self, x: int, y: int):
        for block in self.allBlocks():
            xDiff = block.x - self.x
            yDiff = block.y - self.y
            block.moveTo(x + xDiff, y + yDiff)
        self.x = x
        self.y = y

    def allBlocks(self) -> list[Block]:
        return [block for row in self.blocks for block in row] # python list comprehension is weird


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

    def canMoveGamePiece(self, gamePiece:GamePiece, x:int, y:int) -> bool:
        pass

    def addBlock(self, block: Block):
        """adds block to the game board"""

        if self.blocks[block.x][block.y] != None:
            raise MovementError('game board space not empty')
        self.blocks[block.x][block.y] = block
        self.groundSprites.append(block.sprite)

    def addGamePiece(self, gamePiece:GamePiece):
        for block in gamePiece.allBlocks():
            if block is None:
                continue
            self.blocks[block.x][block.y] = block
            self.playerSprites.append(block.sprite)

    def moveBlock(self, block: Block, x: int, y: int):
        self.removeBlock(block)
        self.blocks[x][y] = block

    def removeBlock(self, block: Block):
        """ remove a block from the game board """
        if (self.blocks[block.x][block.y] is not block):
            raise MovementError('block not found on game board')
        self.blocks[block.x][block.y] = None


class MyPyTrisWindow(arcade.Window):
    """ Main game class """

    def __init__(self):
        super().__init__(GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT, GameConfig.WINDOW_TITLE)
        arcade.set_background_color(arcade.csscolor.LIGHT_PINK)
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.gameBoard = GameBoard(10, 20)

        square = GamePiece(GamePieceConfig.SQUARE)
        square.moveTo(8, 0)
        t = GamePiece(GamePieceConfig.T)
        self.gameBoard.addGamePiece(square)
        self.gameBoard.addGamePiece(t)


    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

        self.gameBoard.draw()

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class MovementError(Error):
    """Exception for invalid movement on the game board"""
    pass


def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()