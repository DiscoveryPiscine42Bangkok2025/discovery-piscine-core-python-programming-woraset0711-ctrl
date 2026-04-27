def checkmate(board):

    lines = [line for line in board.split('\n') if line.strip()]
    if not lines:
        return
    
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) 


    king_pos = None
    for r in range(rows):
        for c in range(len(grid[r])):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos: break

    if not king_pos:
        return

    kr, kc = king_pos

    directions = [
        (-1, 0, "RQ"), (1, 0, "RQ"), (0, -1, "RQ"), (0, 1, "RQ"),   
        (-1, -1, "BQ"), (-1, 1, "BQ"), (1, -1, "BQ"), (1, 1, "BQ") 
    ]

    for dr, dc, enemies in directions:
        r, c = kr + dr, kc + dc

        while 0 <= r < rows and 0 <= c < len(grid[r]):
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
        if 0 <= r < rows and 0 <= c < len(grid[r]):
            if grid[r][c] == 'P':
                print("Success")
                return

    print("Fail")