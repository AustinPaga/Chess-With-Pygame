import pygame
import knight_moves
import bishop_moves
import rook_moves
import queen_moves


whiteKnight2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight.png'), True, False), (26, 26))
whiteKnight3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight2.png'), True, False), (26, 26))
whiteKnight4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight.png'), True, False), (26, 26))
whiteKnight5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight2.png'), True, False), (26, 26))
whiteKnight6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight.png'), True, False), (26, 26))
whiteKnight7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight2.png'), True, False), (26, 26))
whiteKnight8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight.png'), True, False), (26, 26))
whiteKnight9 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight2.png'), True, False), (26, 26))
blackKnight2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight.png'), True, False), (26, 26))
blackKnight3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight2.png'), True, False), (26, 26))
blackKnight4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight.png'), True, False), (26, 26))
blackKnight5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight2.png'), True, False), (26, 26))
blackKnight6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight.png'), True, False), (26, 26))
blackKnight7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight2.png'), True, False), (26, 26))
blackKnight8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight.png'), True, False), (26, 26))
blackKnight9 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight2.png'), True, False), (26, 26))
whiteBishop2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop.png'), True, False), (26, 26))
whiteBishop3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop2.png'), True, False), (26, 26))
whiteBishop4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop.png'), True, False), (26, 26))
whiteBishop5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop2.png'), True, False), (26, 26))
whiteBishop6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop.png'), True, False), (26, 26))
whiteBishop7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop2.png'), True, False), (26, 26))
whiteBishop8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop.png'), True, False), (26, 26))
whiteBishop9 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop2.png'), True, False), (26, 26))
blackBishop2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop.png'), True, False), (26, 26))
blackBishop3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop2.png'), True, False), (26, 26))
blackBishop4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop.png'), True, False), (26, 26))
blackBishop5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop2.png'), True, False), (26, 26))
blackBishop6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop.png'), True, False), (26, 26))
blackBishop7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop2.png'), True, False), (26, 26))
blackBishop8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop.png'), True, False), (26, 26))
blackBishop9 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop2.png'), True, False), (26, 26))
whiteRook2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook.png'), True, False), (26, 26))
whiteRook3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook2.png'), True, False), (26, 26))
whiteRook4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook.png'), True, False), (26, 26))
whiteRook5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook2.png'), True, False), (26, 26))
whiteRook6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook.png'), True, False), (26, 26))
whiteRook7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook2.png'), True, False), (26, 26))
whiteRook8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook.png'), True, False), (26, 26))
whiteRook9 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook2.png'), True, False), (26, 26))
blackRook2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook.png'), True, False), (26, 26))
blackRook3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook2.png'), True, False), (26, 26))
blackRook4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook.png'), True, False), (26, 26))
blackRook5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook2.png'), True, False), (26, 26))
blackRook6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook.png'), True, False), (26, 26))
blackRook7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook2.png'), True, False), (26, 26))
blackRook8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook.png'), True, False), (26, 26))
blackRook9 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook2.png'), True, False), (26, 26))
whiteQueen1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteQueen8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen8 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))

promoted_white_knights = [whiteKnight2, whiteKnight3, whiteKnight4, whiteKnight5, whiteKnight6, whiteKnight7, whiteKnight8, whiteKnight9]
promoted_black_knights = [blackKnight2, blackKnight3, blackKnight4, blackKnight5, blackKnight6, blackKnight7, blackKnight8, blackKnight9]
promoted_white_bishops = [whiteBishop2, whiteBishop3, whiteBishop4, whiteBishop5, whiteBishop6, whiteBishop7, whiteBishop8, whiteBishop9]
promoted_black_bishops = [blackBishop2, blackBishop3, blackBishop4, blackBishop5, blackBishop6, blackBishop7, blackBishop8, blackBishop9]
promoted_white_rooks = [whiteRook2, whiteRook3, whiteRook4, whiteRook5, whiteRook6, whiteRook7, whiteRook8, whiteRook9]
promoted_black_rooks = [blackRook2, blackRook3, blackRook4, blackRook5, blackRook6, blackRook7, blackRook8, blackRook9]
promoted_white_queens = [whiteQueen1, whiteQueen2, whiteQueen3, whiteQueen4, whiteQueen5, whiteQueen6, whiteQueen7, whiteQueen8]
promoted_black_queens = [blackQueen1, blackQueen2, blackQueen3, blackQueen4, blackQueen5, blackQueen6, blackQueen7, blackQueen8]


def instantiate_promoted_pieces(color, type, all_pieces, white_pieces, black_pieces, white_piece_objects, black_piece_objects, board, y, x):
    promoted_object = {}
    if type == "knight" and color == "white":
        c = 10
        for i in promoted_white_knights:
            c += 1
            if i not in all_pieces:
                white_pieces.append(i)
                promoted_object["whiteKnight%d" % c] = None
                all_pieces[i] = [[], "knight"]
                board[y][x] = i
                white_piece_objects.append(knight_moves.Knights(board, i, y, x))
                break

    elif type == "knight" and color == "black":
        c = 10
        for i in promoted_black_knights:
            c += 1
            if i not in all_pieces:
                black_pieces.append(i)
                promoted_object["blackKnight%d" % c] = None
                all_pieces[i] = [[], "knight"]
                board[y][x] = i
                black_piece_objects.append(knight_moves.Knights(board, i, y, x))
                break

    elif type == "bishop" and color == "white":
        c = 10
        for i in promoted_white_bishops:
            c += 1
            if i not in all_pieces:
                white_pieces.append(i)
                promoted_object["whiteBishop%d" % c] = None
                all_pieces[i] = [[], "bishop"]
                board[y][x] = i
                white_piece_objects.append(bishop_moves.Bishops(board, i, y, x))
                break

    elif type == "bishop" and color == "black":
        c = 10
        for i in promoted_black_bishops:
            c += 1
            if i not in all_pieces:
                black_pieces.append(i)
                promoted_object["blackBishop%d" % c] = None
                all_pieces[i] = [[], "bishop"]
                board[y][x] = i
                black_piece_objects.append(bishop_moves.Bishops(board, i, y, x))
                break

    elif type == "rook" and color == "white":
        c = 10
        for i in promoted_white_rooks:
            c += 1
            if i not in all_pieces:
                white_pieces.append(i)
                promoted_object["whiteRook%d" % c] = None
                all_pieces[i] = [[], "rook"]
                board[y][x] = i
                white_piece_objects.append(rook_moves.Rooks(board, i, y, x))
                break

    elif type == "rook" and color == "black":
        c = 10
        for i in promoted_black_rooks:
            c += 1
            if i not in all_pieces:
                black_pieces.append(i)
                promoted_object["blackRook%d" % c] = None
                all_pieces[i] = [[], "rook"]
                board[y][x] = i
                black_piece_objects.append(rook_moves.Rooks(board, i, y, x))
                break

    elif type == "queen" and color == "white":
        c = 10
        for i in promoted_white_queens:
            c += 1
            if i not in all_pieces:
                white_pieces.append(i)
                promoted_object["whiteQueen%d" % c] = None
                all_pieces[i] = [[], "queen"]
                board[y][x] = i
                white_piece_objects.append(queen_moves.Queens(board, i, y, x))
                break

    elif type == "queen" and color == "black":
        c = 10
        for i in promoted_black_queens:
            c += 1
            if i not in all_pieces:
                black_pieces.append(i)
                promoted_object["blackQueen%d" % c] = None
                all_pieces[i] = [[], "queen"]
                board[y][x] = i
                black_piece_objects.append(queen_moves.Queens(board, i, y, x))
                break
