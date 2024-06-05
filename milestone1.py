"""Tic Tac Toe game"""

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


def accept_input():
    """Function that accepts user input and validates it against"""
    choice = input(
        "Please use a number for the row then column using the numbers 1-3 and X or O for the spot designation."
        "For example to place an X on row 1 and column 3 you would enter 1,3,X"
    )
    print(choice)


def init():
    """Function that displays base board and obtains user input"""

    print("Welcome to tic tac toe")
    print(
        """
     | |
    -----
     | |   
    -----
     | |  
     """
    )

    accept_input()


init()
# End-of-file (EOF)
