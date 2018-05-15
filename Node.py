from sys import maxsize
from ChessBoard import ChessBoard


##======================================================================================================================
## Tree Builder
class Node(object):

    def __init__(self, depth, player, chessboard, value=0):
        """  A Node for the decision making of the computer.

        @param Node self: this Node
        @param int depth: the current depth in this Node
        @param int player: either 1 or -1; 1 if this is player, -1 if this is computer
        @param ChessBoard chessboard: the ChessBoard this Node is performing on
        @param int value: the value of this move for the player or the computer
        @rtype: None
        """
        self.depth = depth
        self.player = player
        self.value = value
        self.chessboard = chessboard
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        """ Add all possible moves on the chessboard as children for this Node.

        @param Node self: this Node
        @rtype: None
        """
        if self.depth >= 0:
            # The number of possible moves is based on how many legal moves are left on the chessboard.
            for i in range(9):
                if 0 <= i <= 2:
                    # Check if this tile is free to be taken.
                    if self.chessboard.board[0][2*i] == "0":
                        newChessBoard = self.chessboard.Copy()
                        # Make a new move at the tile (0, i).
                        newChessBoard.MakeMove(0, i, -self.player)
                        # The value of this child Node is dependent on if this will win the player the game.
                        self.children.append(Node(self.depth - 1,
                                                  -self.player,
                                                  newChessBoard,
                                                  self.RealVal(newChessBoard.WinCheck())))
                elif 3 <= i <= 5:
                    # Check if this tile is free to be taken.
                    if self.chessboard.board[2][2*(i-3)] == "0":
                        newChessBoard = self.chessboard.Copy()
                        # Make a new move at the tile (1, i-3).
                        newChessBoard.MakeMove(1, i - 3, -self.player)
                        # The value of this child Node is dependent on if this will win the player the game.
                        self.children.append(Node(self.depth - 1,
                                                  -self.player,
                                                  newChessBoard,
                                                  self.RealVal(newChessBoard.WinCheck())))
                else:
                    # Check if this tile is free to be taken.
                    if self.chessboard.board[4][2*(i-6)] == "0":
                        newChessBoard = self.chessboard.Copy()
                        # Make a new move at the tile (2, i-6).
                        newChessBoard.MakeMove(2, i - 6, -self.player)
                        # The value of this child Node is dependent on if this will win the player the game.
                        self.children.append(Node(self.depth - 1,
                                                  -self.player,
                                                  newChessBoard,
                                                  self.RealVal(newChessBoard.WinCheck())))

    def RealVal(self, value):
        """ Calculates the value for each node; 0 if no significant importance, negative maxsize if leads the human
         player to win, and positive maxsize if leads the computer to win.

        @param Node self: this Node
        @param int value: the raw value of this Node(WinCheck)
        @rtype: int
        """
        # If the human player is playing(WinCheck == 1), return negative infinity; if the computer is
        # winning(WinCheck == -1), return positive infinity; if no one is winning, return 0.
        if value == 1:
            return -maxsize
        elif value == -1:
            return maxsize
        return 0

    ##==================================================================================================================
    ## Minmax Algorithm

    def MinMax(self):
        """ The MinMax algorithm sets the self.value to be the the minimum value of its children when player is -1,
        and the maximum value when player is 1.

        @param Node self: this Node
        @rtype: None
        """
        # Check if it is a leaf Node or if this Node will result in one side winning the game.
        if self.depth == 0 or abs(self.value) == maxsize:
            # Pass because the base case is handled in RealVal when setting up the Node tree.
            pass
        else:
            # Initialise minMaxValue.
            # If the player is the human player(player == 1), make it negative infinity, since we want to get the
            # maximum for bestValue;
            # vice versa.
            minMaxValue = maxsize * -self.player

            for child in self.children:
                # Recursive call for this child Node
                child.MinMax()

                # When this node is computer(player == -1), it is making decision for the human player, therefore
                # we want to minimize the outcome for the human player.
                if self.player == -1:
                    if child.value <= minMaxValue:
                        minMaxValue = child.value
                # Maximize when this node node is human player(player == 1), since it is making decision for the
                # computer.
                else:
                    if minMaxValue <= child.value:
                        minMaxValue = child.value

            self.value = minMaxValue
