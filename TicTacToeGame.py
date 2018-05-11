from sys import maxsize
from Node import Node
from ChessBoard import ChessBoard


##======================================================================================================================
## Game Implementation
def Check(chessboard):
    """ Check if anyone wins the game.

    @param ChessBoard chessboard: the chessboard this game is played on
    @rtype: int
    """
    # Check if this game ends by finishing all the spots.
    if chessboard.MovesLeft() == 0:
        print("*" * 60)
        if chessboard.WinCheck() == 0:
            print("\tOpps, no more spot on the chessboard... New Game? =)")
        elif chessboard.WinCheck() == 1:
            print("\tCongrats you won!!! =D")
        elif chessboard.WinCheck() == -1:
            print("\tComputer won, maybe better luck next time... =(")
        print("*" * 60)
        return 0
    else:
        # Check if this game ends by one side winning.
        if chessboard.WinCheck() != 0:
            print("*" * 60)
            if chessboard.WinCheck() == 1:
                print("\tCongrats you won!!! =D")
            elif chessboard.WinCheck() == -1:
                print("\tComputer won, maybe better luck next time... =(")
            print("*" * 60)
            return 0
        return 1

if __name__ == "__main__":
    currPlayer = 1
    thisChessboard = ChessBoard()
    print("Welcome to the Tic-Tac-Toe Game!!\n")
    print("How to play: Occupy three adjacent tiles to win the game!!\n" +
          "You can only occupy one tile each turn.")

    while thisChessboard.MovesLeft() > 0:
        print("This is the current board: \n")
        thisChessboard.Draw()
        print("Which tile would you want to play? \n")
        # Get the row and column for the play.
        row = int(input("Row (0, 1 or 2): \n"))
        col = int(input("Column (0, 1 or 2): \n"))
        thisChessboard.MakeMove(row, col, currPlayer)
        # The depth of the decision node tree should be dynamically updated as how many moves are left.
        depth = thisChessboard.MovesLeft()
        thisChessboard.Draw()
        # Check if anyone wins the game.
        if thisChessboard.WinCheck() != 1 and thisChessboard.WinCheck() != -1:
            decisionNode = Node(depth, currPlayer, thisChessboard)
            decisionNode.MinMax()
            bestChoice = thisChessboard.board
            bestValue = maxsize * -currPlayer
            # Get the best choice and the corresponding value using the Minmax algorithm.
            for i in range(len(decisionNode.children)):
                child = decisionNode.children[i]

                # Since current player is always the human player(currPlayer == 1),
                # we want to get the maximum value.
                if bestValue <= child.value:
                    bestValue = child.value
                    # Move the chessboard as the child node's chessboard if this is the maximum.
                    bestChoice = child.chessboard.board
            thisChessboard.board = bestChoice

            if thisChessboard.MovesLeft() > 0:
                print("The computer has moved")
                # Used for debugging.
                # print(thisChessboard.board)
            # If the computer wins the game.
            if thisChessboard.WinCheck() == -1:
                thisChessboard.Draw()
                print("Opps computer wins the game... Better luck next time!! :(")
                break
        # If the human player wins the game.
        else:
            print("Congrats you win the game!! =D")
            break
    if thisChessboard.MovesLeft() <= 0:
        print("Opps, the tiles are all occupied... try another game! :)")

