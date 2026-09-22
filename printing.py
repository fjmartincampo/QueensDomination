def printboard(board):
    """Imprime el tablero de ajedrez con 'Q' para las reinas y '-' para casillas vacías."""
    rows = len(board)
    columns = len(board[0])

    # Calculating width for the borders of the chessboard
    width = 2 * columns + 1

    print("+" + "-" * width + "+")

    # Printing the chessboard with 'Q' for queens and '-' for empty spaces
    for i in range(rows):
        print("|", end=" ")
        for j in range(columns):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print("|")

    print("+" + "-" * width + "+")


def printsummary(n, m, objval):
    # Printing the summary of the solution
    print("\n" + "=" * 35)
    print(f"QUEENS DOMINATION {n}x{m}")
    print("=" * 35)
    print(f"Minimum number of queens: {objval}")
    print("=" * 35 + "\n")