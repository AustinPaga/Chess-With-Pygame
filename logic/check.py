def checkIfChecked(all_pieces, board, white_pieces, black_pieces):
    blackInCheck = False
    whiteInCheck = False
    checkers = []

    for key in all_pieces:
        all_pieces[key][0] = []

    for key in all_pieces:
        x = None
        y = None
        for a, b in enumerate(board):
            if key in b:
                y = a
                x = b.index(key)
                break
        if x is not None and y is not None:
            get_adjusted_moves = []
            keyIndex = list(all_pieces.keys()).index(key)
            if 0 <= keyIndex < 8 or 16 <= keyIndex < 24:
                get_adjusted_moves = pawn_legality(key, white_pieces, black_pieces, all_pieces, board, x, y)
            elif 8 <= keyIndex < 10 or 24 <= keyIndex < 26:
                get_adjusted_moves = knight_legality(key, white_pieces, black_pieces, board, x, y)
            elif 10 <= keyIndex < 12 or 26 <= keyIndex < 28:
                get_adjusted_moves = bishop_legality(key, white_pieces, black_pieces, board, x, y)
            elif 12 <= keyIndex < 14 or 28 <= keyIndex < 30:
                get_adjusted_moves = rook_legality(key, white_pieces, black_pieces, board, x, y)
            elif keyIndex == 14 or keyIndex == 30:
                get_adjusted_moves = king_legality(key, white_pieces, black_pieces, all_pieces, board, x, y)
            elif keyIndex == 15 or keyIndex == 31:
                get_adjusted_moves = queen_legality(key, white_pieces, black_pieces, board, x, y)
            else:
                if all_pieces[key][1] == "knight":
                    get_adjusted_moves = knight_legality(key, white_pieces, black_pieces, board, x, y)
                elif all_pieces[key][1] == "bishop":
                    get_adjusted_moves = bishop_legality(key, white_pieces, black_pieces, board, x, y)
                elif all_pieces[key][1] == "rook":
                    get_adjusted_moves = rook_legality(key, white_pieces, black_pieces, board, x, y)
                elif all_pieces[key][1] == "queen":
                    get_adjusted_moves = queen_legality(key, white_pieces, black_pieces, board, x, y)
            all_pieces[key][0] = get_adjusted_moves

    king_coordinates = None
    for a, b in enumerate(board):
        for c in b:
            if c and list(all_pieces)[30] == c:
                king_coordinates = a, b.index(c)
                break
    for key in all_pieces:
        if key in white_pieces and king_coordinates in all_pieces[key][0]:
            checkers.append(key)
            blackInCheck = True

    for a, b in enumerate(board):
        for c in b:
            if c and list(all_pieces)[14] == c:
                king_coordinates = a, b.index(c)
                break
    for key in all_pieces:
        if key in black_pieces and king_coordinates in all_pieces[key][0]:
            checkers.append(key)
            whiteInCheck = True

    return whiteInCheck, blackInCheck, checkers


def pawn_legality(piece, white_pieces, black_pieces, all_pieces, board, x, y):

    pawn_legal_moves = []
    if piece in white_pieces:
        if y != 0:
            if x != 0 and ((board[y - 1][x - 1] in black_pieces) or (y == 3 and board[y][x - 1] in black_pieces and 0 <= black_pieces.index(board[y][x - 1]) < 8 and all_pieces[board[y][x - 1]][1])):
                pawn_legal_moves.append((y - 1, x - 1))
            if x != 7 and ((board[y - 1][x + 1] in black_pieces) or (y == 3 and board[y][x + 1] in black_pieces and 0 <= black_pieces.index(board[y][x + 1]) < 8 and all_pieces[board[y][x + 1]][1])):
                pawn_legal_moves.append((y - 1, x + 1))
            if not board[y - 1][x]:
                pawn_legal_moves.append((y - 1, x))
        if y == 6 and (not board[y - 2][x] and not board[y - 1][x]):
            pawn_legal_moves.append((y - 2, x))

    elif piece in black_pieces:
        if y != 7:
            if x != 0 and ((board[y + 1][x - 1] in white_pieces) or (y == 4 and board[y][x - 1] in white_pieces and 0 <= white_pieces.index(board[y][x - 1]) < 8 and all_pieces[board[y][x - 1]][1])):
                pawn_legal_moves.append((y + 1, x - 1))
            if x != 7 and ((board[y + 1][x + 1] in white_pieces) or (y == 4 and board[y][x + 1] in white_pieces and 0 <= white_pieces.index(board[y][x + 1]) < 8 and all_pieces[board[y][x + 1]][1])):
                pawn_legal_moves.append((y + 1, x + 1))
            if not board[y + 1][x]:
                pawn_legal_moves.append((y + 1, x))
        if y == 1 and (not board[y + 2][x] and not board[y + 1][x]):
            pawn_legal_moves.append((y + 2, x))

    return pawn_legal_moves


def knight_legality(piece, white_pieces, black_pieces, board, x, y):

    knight_legal_moves = []

    if piece in white_pieces:
        if y <= 6 and x <= 5:
            if board[y + 1][x + 2] not in white_pieces:
                knight_legal_moves.append((y + 1, x + 2))
        if y <= 6 and x >= 2:
            if board[y + 1][x - 2] not in white_pieces:
                knight_legal_moves.append((y + 1, x - 2))
        if y <= 5 and x <= 6:
            if board[y + 2][x + 1] not in white_pieces:
                knight_legal_moves.append((y + 2, x + 1))
        if y <= 5 and x >= 1:
            if board[y + 2][x - 1] not in white_pieces:
                knight_legal_moves.append((y + 2, x - 1))
        if y >= 1 and x <= 5:
            if board[y - 1][x + 2] not in white_pieces:
                knight_legal_moves.append((y - 1, x + 2))
        if y >= 1 and x >= 2:
            if board[y - 1][x - 2] not in white_pieces:
                knight_legal_moves.append((y - 1, x - 2))
        if y >= 2 and x <= 6:
            if board[y - 2][x + 1] not in white_pieces:
                knight_legal_moves.append((y - 2, x + 1))
        if y >= 2 and x >= 1:
            if board[y - 2][x - 1] not in white_pieces:
                knight_legal_moves.append((y - 2, x - 1))

    elif piece in black_pieces:
        if y <= 6 and x <= 5:
            if board[y + 1][x + 2] not in black_pieces:
                knight_legal_moves.append((y + 1, x + 2))
        if y <= 6 and x >= 2:
            if board[y + 1][x - 2] not in black_pieces:
                knight_legal_moves.append((y + 1, x - 2))
        if y <= 5 and x <= 6:
            if board[y + 2][x + 1] not in black_pieces:
                knight_legal_moves.append((y + 2, x + 1))
        if y <= 5 and x >= 1:
            if board[y + 2][x - 1] not in black_pieces:
                knight_legal_moves.append((y + 2, x - 1))
        if y >= 1 and x <= 5:
            if board[y - 1][x + 2] not in black_pieces:
                knight_legal_moves.append((y - 1, x + 2))
        if y >= 1 and x >= 2:
            if board[y - 1][x - 2] not in black_pieces:
                knight_legal_moves.append((y - 1, x - 2))
        if y >= 2 and x <= 6:
            if board[y - 2][x + 1] not in black_pieces:
                knight_legal_moves.append((y - 2, x + 1))
        if y >= 2 and x >= 1:
            if board[y - 2][x - 1] not in black_pieces:
                knight_legal_moves.append((y - 2, x - 1))

    return knight_legal_moves


def bishop_legality(piece, white_pieces, black_pieces, board, x, y):
    bishop_legal_moves = []
    not_blocked0 = True
    not_blocked1 = True
    not_blocked2 = True
    not_blocked3 = True

    for c in range(1, 8):

        if piece in white_pieces:
            if y + c < 8 and x + c < 8:
                if not_blocked0 and board[y + c][x + c] not in white_pieces:
                    bishop_legal_moves.append((y + c, x + c))
                if board[y + c][x + c] in white_pieces or board[y + c][x + c] in black_pieces:
                    not_blocked0 = False
            if y - c > -1 and x + c < 8:
                if not_blocked1 and board[y - c][x + c] not in white_pieces:
                    bishop_legal_moves.append((y - c, x + c))
                if board[y - c][x + c] in white_pieces or board[y - c][x + c] in black_pieces:
                    not_blocked1 = False
            if y + c < 8 and x - c > -1:
                if not_blocked2 and board[y + c][x - c] not in white_pieces:
                    bishop_legal_moves.append((y + c, x - c))
                if board[y + c][x - c] in white_pieces or board[y + c][x - c] in black_pieces:
                    not_blocked2 = False
            if y - c > -1 and x - c > -1:
                if not_blocked3 and board[y - c][x - c] not in white_pieces:
                    bishop_legal_moves.append((y - c, x - c))
                if board[y - c][x - c] in white_pieces or board[y - c][x - c] in black_pieces:
                    not_blocked3 = False

        elif piece in black_pieces:
            if y + c < 8 and x + c < 8:
                if not_blocked0 and board[y + c][x + c] not in black_pieces:
                    bishop_legal_moves.append((y + c, x + c))
                if board[y + c][x + c] in white_pieces or board[y + c][x + c] in black_pieces:
                    not_blocked0 = False
            if y - c > -1 and x + c < 8:
                if not_blocked1 and board[y - c][x + c] not in black_pieces:
                    bishop_legal_moves.append((y - c, x + c))
                if board[y - c][x + c] in white_pieces or board[y - c][x + c] in black_pieces:
                    not_blocked1 = False
            if y + c < 8 and x - c > -1:
                if not_blocked2 and board[y + c][x - c] not in black_pieces:
                    bishop_legal_moves.append((y + c, x - c))
                if board[y + c][x - c] in white_pieces or board[y + c][x - c] in black_pieces:
                    not_blocked2 = False
            if y - c > -1 and x - c > -1:
                if not_blocked3 and board[y - c][x - c] not in black_pieces:
                    bishop_legal_moves.append((y - c, x - c))
                if board[y - c][x - c] in white_pieces or board[y - c][x - c] in black_pieces:
                    not_blocked3 = False

    return bishop_legal_moves


def rook_legality(piece, white_pieces, black_pieces, board, x, y):
    rook_legal_moves = []
    not_blocked0 = True
    not_blocked1 = True
    not_blocked2 = True
    not_blocked3 = True

    for c in range(1, 8):
        if piece in white_pieces:
            if y + c < 8:
                if not_blocked0 and board[y + c][x] not in white_pieces:
                    rook_legal_moves.append((y + c, x))
                if board[y + c][x] in white_pieces or board[y + c][x] in black_pieces:
                    not_blocked0 = False
            if y - c > -1:
                if not_blocked1 and board[y - c][x] not in white_pieces:
                    rook_legal_moves.append((y - c, x))
                if board[y - c][x] in white_pieces or board[y - c][x] in black_pieces:
                    not_blocked1 = False
            if x - c > -1:
                if not_blocked2 and board[y][x - c] not in white_pieces:
                    rook_legal_moves.append((y, x - c))
                if board[y][x - c] in white_pieces or board[y][x - c] in black_pieces:
                    not_blocked2 = False
            if x + c < 8:
                if not_blocked3 and board[y][x + c] not in white_pieces:
                    rook_legal_moves.append((y, x + c))
                if board[y][x + c] in white_pieces or board[y][x + c] in black_pieces:
                    not_blocked3 = False

        elif piece in black_pieces:
            if y + c < 8:
                if not_blocked0 and board[y + c][x] not in black_pieces:
                    rook_legal_moves.append((y + c, x))
                if board[y + c][x] in white_pieces or board[y + c][x] in black_pieces:
                    not_blocked0 = False
            if y - c > -1:
                if not_blocked1 and board[y - c][x] not in black_pieces:
                    rook_legal_moves.append((y - c, x))
                if board[y - c][x] in white_pieces or board[y - c][x] in black_pieces:
                    not_blocked1 = False
            if x - c > -1:
                if not_blocked2 and board[y][x - c] not in black_pieces:
                    rook_legal_moves.append((y, x - c))
                if board[y][x - c] in white_pieces or board[y][x - c] in black_pieces:
                    not_blocked2 = False
            if x + c < 8:
                if not_blocked3 and board[y][x + c] not in black_pieces:
                    rook_legal_moves.append((y, x + c))
                if board[y][x + c] in white_pieces or board[y][x + c] in black_pieces:
                    not_blocked3 = False

    return rook_legal_moves


def king_legality(piece, white_pieces, black_pieces, all_pieces, board, x, y):
    king_legal_moves = []
    if piece in white_pieces:
        if x != 0 and board[y][x - 1] not in white_pieces:
            king_legal_moves.append((y, x - 1))
        if x != 7 and board[y][x + 1] not in white_pieces:
            king_legal_moves.append((y, x + 1))
        if y != 0 and board[y - 1][x] not in white_pieces:
            king_legal_moves.append((y - 1, x))
        if y != 7 and board[y + 1][x] not in white_pieces:
            king_legal_moves.append((y + 1, x))
        if x != 7 and y != 0 and board[y - 1][x + 1] not in white_pieces:
            king_legal_moves.append((y - 1, x + 1))
        if x != 7 and y != 7 and board[y + 1][x + 1] not in white_pieces:
            king_legal_moves.append((y + 1, x + 1))
        if x != 0 and y != 7 and board[y + 1][x - 1] not in white_pieces:
            king_legal_moves.append((y + 1, x - 1))
        if x != 0 and y != 0 and board[y - 1][x - 1] not in white_pieces:
            king_legal_moves.append((y - 1, x - 1))
        if not all_pieces[piece][1]:
            if board[y][x + 3] and not all_pieces[board[y][x + 3]][1] and not board[y][x + 2] and not board[y][x + 1]:
                castle_blocked = False
                for piece in black_pieces:
                    if (y, x + 2) in all_pieces[piece][0] or (y, x + 1) in all_pieces[piece][0]:
                        castle_blocked = True
                if not castle_blocked:
                    king_legal_moves.append((y, x + 2))
            if board[y][x - 4] and not all_pieces[board[y][x - 4]][1] and not board[y][x - 3] and not board[y][x - 2] and not board[y][x - 1]:
                castle_blocked = False
                for piece in black_pieces:
                    if (y, x - 2) in all_pieces[piece][0] or (y, x - 1) in all_pieces[piece][0]:
                        castle_blocked = True
                if not castle_blocked:
                    king_legal_moves.append((y, x - 2))

    elif piece in black_pieces:
        if x != 0 and board[y][x - 1] not in black_pieces:
            king_legal_moves.append((y, x - 1))
        if x != 7 and board[y][x + 1] not in black_pieces:
            king_legal_moves.append((y, x + 1))
        if y != 0 and board[y - 1][x] not in black_pieces:
            king_legal_moves.append((y - 1, x))
        if y != 7 and board[y + 1][x] not in black_pieces:
            king_legal_moves.append((y + 1, x))
        if x != 7 and y != 0 and board[y - 1][x + 1] not in black_pieces:
            king_legal_moves.append((y - 1, x + 1))
        if x != 7 and y != 7 and board[y + 1][x + 1] not in black_pieces:
            king_legal_moves.append((y + 1, x + 1))
        if x != 0 and y != 7 and board[y + 1][x - 1] not in black_pieces:
            king_legal_moves.append((y + 1, x - 1))
        if x != 0 and y != 0 and board[y - 1][x - 1] not in black_pieces:
            king_legal_moves.append((y - 1, x - 1))
        if not all_pieces[piece][1]:
            if board[y][x + 3] and not all_pieces[board[y][x + 3]][1] and not board[y][x + 2] and not board[y][x + 1]:
                castle_blocked = False
                for piece in white_pieces:
                    if (y, x + 2) in all_pieces[piece][0] or (y, x + 1) in all_pieces[piece][0]:
                        castle_blocked = True
                if not castle_blocked:
                    king_legal_moves.append((y, x + 2))
            if board[y][x - 4] and not all_pieces[board[y][x - 4]][1] and not board[y][x - 3] and not board[y][x - 2] and not board[y][x - 1]:
                castle_blocked = False
                for piece in white_pieces:
                    if (y, x - 2) in all_pieces[piece][0] or (y, x - 1) in all_pieces[piece][0]:
                        castle_blocked = True
                if not castle_blocked:
                    king_legal_moves.append((y, x - 2))

    return king_legal_moves


def queen_legality(piece, white_pieces, black_pieces, board, x, y):
    queen_legal_moves = []
    not_blocked0 = True
    not_blocked1 = True
    not_blocked2 = True
    not_blocked3 = True
    not_blocked4 = True
    not_blocked5 = True
    not_blocked6 = True
    not_blocked7 = True

    for c in range(1, 8):

        if piece in white_pieces:
            if y + c < 8 and x + c < 8:
                if not_blocked0 and board[y + c][x + c] not in white_pieces:
                    queen_legal_moves.append((y + c, x + c))
                if board[y + c][x + c] in white_pieces or board[y + c][x + c] in black_pieces:
                    not_blocked0 = False
            if y - c > -1 and x + c < 8:
                if not_blocked1 and board[y - c][x + c] not in white_pieces:
                    queen_legal_moves.append((y - c, x + c))
                if board[y - c][x + c] in white_pieces or board[y - c][x + c] in black_pieces:
                    not_blocked1 = False
            if y + c < 8 and x - c > -1:
                if not_blocked2 and board[y + c][x - c] not in white_pieces:
                    queen_legal_moves.append((y + c, x - c))
                if board[y + c][x - c] in white_pieces or board[y + c][x - c] in black_pieces:
                    not_blocked2 = False
            if y - c > -1 and x - c > -1:
                if not_blocked3 and board[y - c][x - c] not in white_pieces:
                    queen_legal_moves.append((y - c, x - c))
                if board[y - c][x - c] in white_pieces or board[y - c][x - c] in black_pieces:
                    not_blocked3 = False
            if y + c < 8:
                if not_blocked4 and board[y + c][x] not in white_pieces:
                    queen_legal_moves.append((y + c, x))
                if board[y + c][x] in white_pieces or board[y + c][x] in black_pieces:
                    not_blocked4 = False
            if y - c > -1:
                if not_blocked5 and board[y - c][x] not in white_pieces:
                    queen_legal_moves.append((y - c, x))
                if board[y - c][x] in white_pieces or board[y - c][x] in black_pieces:
                    not_blocked5 = False
            if x - c > -1:
                if not_blocked6 and board[y][x - c] not in white_pieces:
                    queen_legal_moves.append((y, x - c))
                if board[y][x - c] in white_pieces or board[y][x - c] in black_pieces:
                    not_blocked6 = False
            if x + c < 8:
                if not_blocked7 and board[y][x + c] not in white_pieces:
                    queen_legal_moves.append((y, x + c))
                if board[y][x + c] in white_pieces or board[y][x + c] in black_pieces:
                    not_blocked7 = False

        elif piece in black_pieces:
            if y + c < 8 and x + c < 8:
                if not_blocked0 and board[y + c][x + c] not in black_pieces:
                    queen_legal_moves.append((y + c, x + c))
                if board[y + c][x + c] in white_pieces or board[y + c][x + c] in black_pieces:
                    not_blocked0 = False
            if y - c > -1 and x + c < 8:
                if not_blocked1 and board[y - c][x + c] not in black_pieces:
                    queen_legal_moves.append((y - c, x + c))
                if board[y - c][x + c] in white_pieces or board[y - c][x + c] in black_pieces:
                    not_blocked1 = False
            if y + c < 8 and x - c > -1:
                if not_blocked2 and board[y + c][x - c] not in black_pieces:
                    queen_legal_moves.append((y + c, x - c))
                if board[y + c][x - c] in white_pieces or board[y + c][x - c] in black_pieces:
                    not_blocked2 = False
            if y - c > -1 and x - c > -1:
                if not_blocked3 and board[y - c][x - c] not in black_pieces:
                    queen_legal_moves.append((y - c, x - c))
                if board[y - c][x - c] in white_pieces or board[y - c][x - c] in black_pieces:
                    not_blocked3 = False
            if y + c < 8:
                if not_blocked4 and board[y + c][x] not in black_pieces:
                    queen_legal_moves.append((y + c, x))
                if board[y + c][x] in white_pieces or board[y + c][x] in black_pieces:
                    not_blocked4 = False
            if y - c > -1:
                if not_blocked5 and board[y - c][x] not in black_pieces:
                    queen_legal_moves.append((y - c, x))
                if board[y - c][x] in white_pieces or board[y - c][x] in black_pieces:
                    not_blocked5 = False
            if x - c > -1:
                if not_blocked6 and board[y][x - c] not in black_pieces:
                    queen_legal_moves.append((y, x - c))
                if board[y][x - c] in white_pieces or board[y][x - c] in black_pieces:
                    not_blocked6 = False
            if x + c < 8:
                if not_blocked7 and board[y][x + c] not in black_pieces:
                    queen_legal_moves.append((y, x + c))
                if board[y][x + c] in white_pieces or board[y][x + c] in black_pieces:
                    not_blocked7 = False

    return queen_legal_moves
