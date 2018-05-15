class ChessBoard(object):
    """
    A chessboard Object for this Tic-Tac-Toe game.
    """

    def __init__(self):
        """ Set up the chessboard.

        @param ChessBoard self: this ChessBoard
        @rtype: None
        """
        self.board = []
        self.SetUpChessBoard()

    def SetUpChessBoard(self):
        """ Set up the look of the chessboard.

        @param ChessBoard self: this ChessBoard
        @rtype: None
        """
        for i in range(5):
            # Set up the five rows as five lists.
            self.board.append([])
            # If this is an even row:
            if i % 2 == 0:
                # Set up the columns.
                for j in range(5):
                    # If this is an even column:
                    if j % 2 == 0:
                        self.board[i].append("0")
                    # If this is an odd column:
                    else:
                        self.board[i].append("|")
            # If this is an odd row:
            else:
                for j in range(5):
                    # If this is an even column:
                    if j % 2 == 0:
                        self.board[i].append("-")
                    # If this is an odd column:
                    else:
                        self.board[i].append("+")

    def Draw(self):
        """ Draw this chessboard.

        @param ChessBoard self: this ChessBoard
        @rtype: None
        """
        # Set up the String representation of this chessboard.
        s = ""
        for i in range(len(self.board)):
            # If this is an even row:
            if i % 2 == 0:
                for j in range(len(self.board[i])):
                    # If this spot is unwritten:
                    if self.board[i][j] == "0":
                        s += " "
                    elif self.board[i][j] == "-1":
                        s += "O"
                    elif self.board[i][j] == "1":
                        s += "X"
                    else:
                        s += self.board[i][j]
                        # If this is the last column.
                    if j == 4:
                        s += "\n"
            # If this is an odd row:
            else:
                for j in range(len(self.board[i])):
                    s += self.board[i][j]
                    # If this is the last column.
                    if j == 4:
                        s += "\n"
        print(s)

    def MovesLeft(self):
        """ Return how many spots on the chessboard is left available.

        @param ChessBoard self: this ChessBoard
        @rtype: int
        """
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "0":
                    count += 1
        return count

    def WinCheck(self):
        """ Return 1 if the player wins, -1 if the computer wins, 0 if no one wins.

        @param ChessBoard self: this ChessBoard
        @rtype: int
        """
        # Check if one of the rows have the same mark.
        for i in range(len(self.board)):
            # If this is an even row.
            if i % 2 == 0:
                if (self.board[i][0] == self.board[i][2]) and (self.board[i][0] == self.board[i][4]):
                    if self.board[i][0] == "1":
                        return 1
                    elif self.board[i][0] == "-1":
                        return -1
        # Check if one of the columns have the same mark.
        for j in range(5):
            # If this is an even column.
            if j % 2 == 0:
                if (self.board[0][j] == self.board[2][j]) and (self.board[0][j] == self.board[4][j]):
                    if self.board[0][j] == "1":
                        return 1
                    elif self.board[0][j] == "-1":
                        return -1
        # Check if one of thw two crosses have the same mark.
        for k in range(5):
            if (self.board[0][0] == self.board[2][2]) and (self.board[0][0] == self.board[4][4]):
                if self.board[0][0] == "1":
                    return 1
                elif self.board[0][0] == "-1":
                    return -1
            elif (self.board[0][4] == self.board[2][2]) and (self.board[0][4] == self.board[4][0]):
                if self.board[0][4] == "1":
                    return 1
                elif self.board[0][4] == "-1":
                    return -1
        # Return 0 otherwise.
        return 0

    def MakeMove(self, row, col, player):
        """ Make the move of occupying a tile.

        @param ChessBoard self: this ChessBoard
        @param int row: the row of the tile
        @param int col: the column of the tile
        @param int player: either 1 or -1; 1 if this is player, -1 if this is computer
        @rtype: None
        """
        if self.board[2*row][2*col] == "0":
            self.board[2*row][2*col] = str(player)
        else:
            print("This tile is already taken, please take a new tile.\n")
            print("This is the current board: \n")
            self.Draw()
            print("Which tile would you want to play? \n")
            # Get the row and column for the play.
            i_row = int(input("Row (0, 1 or 2): \n"))
            i_col = int(input("Column (0, 1 or 2): \n"))
            self.MakeMove(i_row, i_col, player)

    def Copy(self):
        """ Returns a copy of this ChessBoard.

        @param ChessBoard self: this ChessBoard
        @rtype: ChessBoard
        """
        newChessBoard = ChessBoard()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                newChessBoard.board[i][j] = self.board[i][j]
        return newChessBoard


if __name__ == "__main__":
    chessboard = ChessBoard()
    chessboard.Draw()
    print(chessboard.MovesLeft())
    print(chessboard.WinCheck())
