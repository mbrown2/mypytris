""" My PyTris is a tetris style game made with Python Arcade

Its cool because I made it.
"""

from enum import Enum
import arcade
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

    def __init__(self, x: int, y: int):
        self.sprite = arcade.Sprite(r'mypytris/sprites/Blocks_01_64x64_Alt_00_001.png', GameConfig.BLOCK_SCALE)
        self.moveTo(x, y)

    def moveTo(self, x: int, y: int):
        self.x = x
        self.y = y

        # scale position from block grid to screen pixels
        self.sprite.left = x * GameConfig.BLOCK_PX
        self.sprite.bottom = y * GameConfig.BLOCK_PX
        return self

class GamePiece:
    """ Game pieces are composed of multiple blocks that form a game piece shape """

    def __init__(self, x=0, y=0):
        self.blockMap = [[True, True], # [(0,0), (0,1)],
                         [True, True]] # [(1,0), (1,1)]
        self.x = x
        self.y = y
        self.blocks: list[Block] = []

    def create(self):
        maxY = len(self.blockMap)
        maxX = len(self.blockMap[0])
        for y in range(maxY):
            for x in range(maxX):
                if self.blockMap[y][x]:
                    self.blocks.append(Block(self.y + y, self.x + x))
        return self

    def moveTo(self, x: int, y: int):
        for block in self.blocks:
            xDiff = block.x - self.x
            yDiff = block.y - self.y
            block.moveTo(x + xDiff, y + yDiff)
        self.x = x
        self.y = y

class MyPyTrisWindow(arcade.Window):
    """ Main game class """

    def __init__(self):
        super().__init__(GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT, GameConfig.WINDOW_TITLE)
        arcade.set_background_color(arcade.csscolor.LIGHT_PINK)
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.playerSprites = SpriteList()
        self.groundSprites = SpriteList()

        square = GamePiece(0, 0).create()
        square.moveTo(8, 0)
        self.addGamePiece(square)

    def addGamePiece(self, gamePiece: GamePiece):
        for block in gamePiece.blocks:
            self.playerSprites.append(block.sprite)

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

        self.playerSprites.draw()
        self.groundSprites.draw()


def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()