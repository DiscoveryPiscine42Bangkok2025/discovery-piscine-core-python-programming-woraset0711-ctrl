def checkmate(board):

    lines = [line.strip() for line in board.split('\n') if line.strip()]
    if not lines:
        return

    rows = len(lines)
    allowed_chars = set("KQRBP.") 


    for line in lines:

        if len(line) != rows:
            print("Fail (Not a square board)")
            return

        for char in line:
            if char not in allowed_chars:
                print(f"Fail (Invalid character: {char})")
                return

    grid = [list(line) for line in lines]

    king_pos = None
    for r in range(rows):
        for c in range(rows):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos: break

    if not king_pos:
        print("Fail (No King found)")
        return

    kr, kc = king_pos


    directions = [
        (-1, 0, "RQ"), (1, 0, "RQ"), (0, -1, "RQ"), (0, 1, "RQ"), 
        (-1, -1, "BQ"), (-1, 1, "BQ"), (1, -1, "BQ"), (1, 1, "BQ") 
    ]

    for dr, dc, enemies in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < rows and 0 <= c < rows:
            piece = grid[r][c]
            if piece != '.':
                if piece in enemies:
                    print("Success")
                    return
                break 
            r += dr
            c += dc

    pawn_threats = [(1, -1), (1, 1)]
    for dr, dc in pawn_threats:
        r, c = kr + dr, kc + dc
        if 0 <= r < rows and 0 <= c < rows:
            if grid[r][c] == 'P':
                print("Success")
                return

    print("Fail")