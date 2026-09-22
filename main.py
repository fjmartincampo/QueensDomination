from model import solve
from printing import printsummary, printboard
from reading import getdimensions

# Queens domination: Minimum number of queens to dominate a chessboard
print("Queens domination: Minimum number of queens to dominate a chessboard")
print("--------------------------------------------------------------------")

# Obtaining the dimensions of the chessboard
n, m = getdimensions()

# Building and solving the optimization model
status, objval, board = solve(n, m)

# Showing the results
if board is not None:
    printsummary(n, m, objval)
    printboard(board)
else:
    print(f"\nNo solution found. Gurobi status: {status}")