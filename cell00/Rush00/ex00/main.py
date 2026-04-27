from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
...."""
    
    board2 = """\
..
.K
B."""

    print("Test 1: ", end="")
    checkmate(board1)
    
    print("Test 2: ", end="")
    checkmate(board2) 

if __name__ == "__main__":
    main()