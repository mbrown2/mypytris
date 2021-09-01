""" My PyTris is a tetris style game made with Python Arcade

Its cool because I made it.
"""

import arcade

# Constants
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 900
WINDOW_TITLE = "MyPyTris"
BLOCK_PX = 45 # 45px blocks on screen
SPRITE_PX = 64 # 64px sprite
BLOCK_SCALE = BLOCK_PX/SPRITE_PX # sprite scale ratio


class MyPyTrisWindow(arcade.Window):
    """ Main game class """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.csscolor.LIGHT_PINK)
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.playerBlockList = arcade.SpriteList()
        self.groundBlockList = arcade.SpriteList(use_spatial_hash=True)
        
        
        for x in range(0, 10):
            block = Block(x, 0)
            self.groundBlockList.append(block.sprite)

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

        self.playerBlockList.draw()
        self.groundBlockList.draw()

class Block:
    """ Single block class """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite('mypytris\sprites\Blocks_01_64x64_Alt_00_001.png', BLOCK_SCALE)
        
        # scale position from block grid to screen pixels
        self.sprite.left = x * BLOCK_PX
        self.sprite.bottom = y * BLOCK_PX

class GamePiece:
    """ Game pieces are composed of multiple blocks that form a game piece shape """

    def __init__(self):
        pass


def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()