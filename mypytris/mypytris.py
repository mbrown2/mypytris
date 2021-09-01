""" My PyTris is a tetris style game made with Python Arcade

Its cool because I made it.
"""

import arcade

# Constants
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 900
WINDOW_TITLE = "MyPyTris"

class MyPyTrisWindow(arcade.Window):
    """ Main game class """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.csscolor.LIGHT_PINK)
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()