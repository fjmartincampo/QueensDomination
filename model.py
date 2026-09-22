from gurobipy import *

def solve(n: int, m: int):

    # Create the Gurobi model
    model = Model("QueensDomination")

    # Decision variables: x[i, j] = 1 if there is a queen in cell (i, j), 0 otherwise
    x = model.addVars(n, m, vtype=GRB.BINARY, name="x")

    # Objective function: Minimize the total number of queens
    model.setObjective(x.sum(), GRB.MINIMIZE)

    # Dominance constraint: Each square (i, j) must be attacked by at least one queen
    for i in range(n):
        for j in range(m):
            # Identify all cells (r, c) from where a queen dominates (i, j)
            attackers = [
                x[r, c]
                for r in range(n)
                for c in range(m)
                if r == i or c == j or abs(r - i) == abs(c - j)
            ]

            # The sum of the queens in these cells must be >= 1
            model.addConstr(quicksum(attackers) >= 1, name=f"Domination_{i}_{j}")

    # Hide Gurobi output and optimize the model
    model.setParam("OutputFlag", 0)

    # Optimize the model
    model.optimize()

    # Process results
    if model.status == GRB.OPTIMAL:
        # Create matrix with the results (1 for queen, 0 for empty)
        board = [[int(round(x[i, j].X)) for j in range(m)] for i in range(n)]
        return model.status, int(round(model.ObjVal)), board
    else:
        return model.status, None, None