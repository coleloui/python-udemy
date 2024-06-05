"""Tic Tac Toe game"""


def accept_input(base):
    """Function that accepts user input and validates it against"""

    choice = input(
        "Please use a number for the row then column using the numbers 1-3 and X or O for the spot designation."
        "For example to place an X on row 1 and column 3 you would enter 1,3,X\n"
    )

    row, column, value = choice.split(",")

    if row.int() not in [1, 2, 3] or column.int() not in [1, 2, 3]:
        print("you stupid")
        accept_input(base)
    elif value.lower() != "x" or value.lower() != "o":
        print("you stupid")
        accept_input(base)
    elif base["row{row}column{column}"].format(row, column).lower() == value.lower():
        print("you stupid")
        accept_input(base)
    else:
        value = base["row{row}column{column}"].format(row, column)
        return base


def display(row, column, choice):
    """places choice where it belongs and returns input to user"""
    return row, column, choice


def init():
    """Function that displays base board and obtains user input"""

    base = {
        "row1column1": " ",
        "row1column2": " ",
        "row1column3": " ",
        "row2column1": " ",
        "row2column2": " ",
        "row2column3": " ",
        "row3column1": " ",
        "row3column2": " ",
        "row3column3": " ",
    }

    print("Welcome to tic tac toe")
    print(
        """
    {row1column1}|{row1column2}|{row1column3}
    -----
    {row2column2}|{row2column2}|{row2column3}
    -----
    {row3column1}|{row3column2}|{row3column3}
     """.format(
            **base
        )
    )

    choice_arr = accept_input(base)
    new_base = display(base, *choice_arr)
    # check winner and recurse if necessary


init()
# End-of-file (EOF)
