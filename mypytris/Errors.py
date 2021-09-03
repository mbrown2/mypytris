class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class MovementError(Error):
    """Exception for invalid movement on the game board"""
    pass