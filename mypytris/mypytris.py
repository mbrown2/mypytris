""" My PyTris is a tetris style game made with Python Arcade

Its cool because I made it.
"""

import Game
import GamePiece
import arcade

class MyPyTrisWindow(arcade.Window):
    """ Main game class """

    def __init__(self):
        super().__init__(Game.GameConfig.SCREEN_WIDTH, Game.GameConfig.SCREEN_HEIGHT, Game.GameConfig.WINDOW_TITLE)
        arcade.set_background_color(arcade.csscolor.LIGHT_PINK)
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.gameBoard = Game.GameBoard(10, 20)

        gamePiece = GamePiece.nextPiece()
        self.gameBoard.addGamePiece(gamePiece)
        


    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

        self.gameBoard.draw()


def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()