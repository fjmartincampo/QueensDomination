def getdimensions():
    # Asking for number of rows and columns for the chessboard
    while True:
        try:
            n = int(input("Number of rows (n): "))
            m = int(input("Number of columns (m): "))
            if n > 0 and m > 0:
                return n, m
            print(
                "Error: The dimensions must be positive integers.\n"
            )
        except ValueError:
            print(
                "Error: Please enter only positive integer values.\n"
            )