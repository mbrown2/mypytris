import numpy as np
import arcade
import Game
from enum import IntEnum
import random

class Block:
    """ Single block class """

    def __init__(self, x:int = 0, y:int = 0, imgPath = r'mypytris/sprites/Blocks_01_64x64_Alt_00_001.png'):
        self.sprite = arcade.Sprite(imgPath, Game.GameConfig.BLOCK_SCALE)
        self.moveTo(x, y)

    def moveTo(self, x:int, y:int) -> None:
        # scale position from block grid to screen pixels
        self.sprite.left = x * Game.GameConfig.BLOCK_PX
        self.sprite.bottom = y * Game.GameConfig.BLOCK_PX
        self.x = x
        self.y = y

class ShapeEnum(IntEnum):
    SQUARE  = 0
    T       = 1
    PLUS    = 2
    L       = 3
    J       = 4
    S       = 5
    TWO     = 6
    I       = 7

class GamePieceConfig():

    def __init__(self, imgPath:str, shape:list[list[int]]) -> None:
        self.shape = shape
        self.imgPath = imgPath

GamePieceConfig.SQUARE  = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_006.png', 
                                          np.array([[1,1],
                                                    [1,1]], dtype=np.byte))
GamePieceConfig.T       = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_003.png', 
                                          np.array([[0,0,0],
                                                    [0,1,0],
                                                    [1,1,1]], dtype=np.byte))
GamePieceConfig.PLUS    = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_004.png', 
                                          np.array([[0,1,0],
                                                    [1,1,1],
                                                    [0,1,0]], dtype=np.byte))
GamePieceConfig.L       = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_005.png', 
                                          np.array([[0,1,0],
                                                    [0,1,0],
                                                    [0,1,1]], dtype=np.byte))
GamePieceConfig.J       = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_005.png', 
                                          np.array([[0,1,0],
                                                    [0,1,0],
                                                    [1,1,0]], dtype=np.byte))
GamePieceConfig.S       = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_002.png', 
                                          np.array([[0,0,0],
                                                    [0,1,1],
                                                    [1,1,0]], dtype=np.byte))
GamePieceConfig.TWO     = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_002.png', 
                                          np.array([[0,0,0],
                                                    [1,1,0],
                                                    [0,1,1]], dtype=np.byte))
GamePieceConfig.I       = GamePieceConfig(r'mypytris/sprites/Blocks_01_64x64_Alt_00_007.png', 
                                          np.array([[0,1,0,0],
                                                    [0,1,0,0],
                                                    [0,1,0,0],
                                                    [0,1,0,0]], dtype=np.byte))
GamePieceConfig.ALL = [GamePieceConfig.SQUARE, GamePieceConfig.T, GamePieceConfig.PLUS,
                       GamePieceConfig.L, GamePieceConfig.J, GamePieceConfig.S, GamePieceConfig.TWO,
                       GamePieceConfig.I]
GamePieceConfig.DICT = {
    ShapeEnum.SQUARE: GamePieceConfig.SQUARE,
    ShapeEnum.T:      GamePieceConfig.T,
    ShapeEnum.PLUS:   GamePieceConfig.PLUS,
    ShapeEnum.L:      GamePieceConfig.L,
    ShapeEnum.J:      GamePieceConfig.J,
    ShapeEnum.S:      GamePieceConfig.S,
    ShapeEnum.TWO:    GamePieceConfig.TWO,
    ShapeEnum.I:      GamePieceConfig.I }

class GamePiece:
    """ Game pieces are composed of multiple blocks that form a game piece shape """

    def __init__(self, config:GamePieceConfig):
        self.config = config
        self.size = len(self.config.shape)
        self.blocks = [[] for y in range(self.size)]
        for y in range(self.size):
            self.blocks.append([])
            for x in range(self.size):
                shapeFlipped = np.flipud(self.config.shape)
                self.blocks[y].append(Block(x, y, config.imgPath) if shapeFlipped[y][x] == 1 else None)

        #self.blocks = [[Block(x,y, self.config.imgPath) for y in reversed(range(self.size)) if self.config.shape[x][y] == 1] for x in range(self.size)]
        self.x = 0
        self.y = 0

    def moveTo(self, x: int, y: int):
        for block in self.allBlocks():
            if block is None:
                continue
            xDiff = block.x - self.x
            yDiff = block.y - self.y
            block.moveTo(x + xDiff, y + yDiff)
        self.x = x
        self.y = y

    def move(self, changeInX:int, changeInY:int):
        self.moveTo(self.x + changeInX, self.y + changeInY)

    def allBlocks(self) -> list[Block]:
        return [block for row in self.blocks for block in row] # python list comprehension is weird

def nextPiece():
    return GamePiece(GamePieceConfig.ALL[random.randint(0, len(GamePieceConfig.ALL) - 1)])