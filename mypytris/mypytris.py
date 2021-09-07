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
        self.gameEngine = Game.GameEngine(self.gameBoard)

        self.gameBoard.spawnPlayerPiece()

    def on_update(self, delta_time: float):
        self.gameEngine.on_update(delta_time)
        
    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here

        self.gameBoard.draw()

    def on_key_press(self, key: int, modifiers: int):
        board = self.gameBoard
        if key == arcade.key.UP or key == arcade.key.W:
            if modifiers & arcade.key.MOD_SHIFT == 1:
                board.moveGamePiece(board.playerPiece, board.playerPiece.x, board.playerPiece.y + 1)
            else:
                board.rotateGamePiece(board.playerPiece)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            board.moveGamePiece(board.playerPiece, board.playerPiece.x, board.playerPiece.y - 1)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            board.moveGamePiece(board.playerPiece, board.playerPiece.x - 1, board.playerPiece.y)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            board.moveGamePiece(board.playerPiece, board.playerPiece.x + 1, board.playerPiece.y)


def main():
    """Main method"""
    window = MyPyTrisWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()