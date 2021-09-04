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

        self.playerPiece = GamePiece.nextPiece()
        self.gameBoard.addGamePiece(self.playerPiece)
        


    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

        self.gameBoard.draw()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            if modifiers & arcade.key.MOD_SHIFT == 1:
                self.playerPiece.rotate()
            else:
                self.gameBoard.moveGamePiece(self.playerPiece, self.playerPiece.x, self.playerPiece.y + 1)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.gameBoard.moveGamePiece(self.playerPiece, self.playerPiece.x, self.playerPiece.y - 1)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.gameBoard.moveGamePiece(self.playerPiece, self.playerPiece.x - 1, self.playerPiece.y)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.gameBoard.moveGamePiece(self.playerPiece, self.playerPiece.x + 1, self.playerPiece.y)


def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()