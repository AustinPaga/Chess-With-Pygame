import pygame
import pawn_moves
import knight_moves
import bishop_moves
import rook_moves
import queen_moves
import king_moves

whitePawn0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn.png'), True, False), (26, 26))
whitePawn1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn1.png'), True, False), (26, 26))
whitePawn2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn2.png'), True, False), (26, 26))
whitePawn3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn3.png'), True, False), (26, 26))
whitePawn4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn4.png'), True, False), (26, 26))
whitePawn5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn5.png'), True, False), (26, 26))
whitePawn6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn6.png'), True, False), (26, 26))
whitePawn7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhitePawn7.png'), True, False), (26, 26))
blackPawn0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn.png'), True, False), (26, 26))
blackPawn1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn1.png'), True, False), (26, 26))
blackPawn2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn2.png'), True, False), (26, 26))
blackPawn3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn3.png'), True, False), (26, 26))
blackPawn4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn4.png'), True, False), (26, 26))
blackPawn5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn5.png'), True, False), (26, 26))
blackPawn6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn6.png'), True, False), (26, 26))
blackPawn7 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackPawn7.png'), True, False), (26, 26))
whiteKnight0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight.png'), True, False), (26, 26))
whiteKnight1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKnight2.png'), True, False), (26, 26))
blackKnight0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight.png'), True, False), (26, 26))
blackKnight1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKnight2.png'), True, False), (26, 26))
whiteBishop0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop.png'), True, False), (26, 26))
whiteBishop1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteBishop2.png'), True, False), (26, 26))
blackBishop0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop.png'), True, False), (26, 26))
blackBishop1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackBishop2.png'), True, False), (26, 26))
whiteRook0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook.png'), True, False), (26, 26))
whiteRook1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteRook2.png'), True, False), (26, 26))
blackRook0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook.png'), True, False), (26, 26))
blackRook1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackRook2.png'), True, False), (26, 26))
whiteQueen0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteQueen.png'), True, False), (26, 26))
blackQueen0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackQueen.png'), True, False), (26, 26))
whiteKing0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/WhiteKing.png'), True, False), (26, 26))
blackKing0 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('chess_pieces/BlackKing.png'), True, False), (26, 26))


def instantiate_white_pieces(board):
    whiteAPawn = pawn_moves.Pawns(board, whitePawn0, 0, 6)
    whiteBPawn = pawn_moves.Pawns(board, whitePawn1, 1, 6)
    whiteCPawn = pawn_moves.Pawns(board, whitePawn2, 2, 6)
    whiteDPawn = pawn_moves.Pawns(board, whitePawn3, 3, 6)
    whiteEPawn = pawn_moves.Pawns(board, whitePawn4, 4, 6)
    whiteFPawn = pawn_moves.Pawns(board, whitePawn5, 5, 6)
    whiteGPawn = pawn_moves.Pawns(board, whitePawn6, 6, 6)
    whiteHPawn = pawn_moves.Pawns(board, whitePawn7, 7, 6)
    whiteBKnight = knight_moves.Knights(board, whiteKnight0, 1, 7)
    whiteGKnight = knight_moves.Knights(board, whiteKnight1, 6, 7)
    whiteCBishop = bishop_moves.Bishops(board, whiteBishop0, 2, 7)
    whiteFBishop = bishop_moves.Bishops(board, whiteBishop1, 5, 7)
    whiteARook = rook_moves.Rooks(board, whiteRook0, 0, 7)
    whiteHRook = rook_moves.Rooks(board, whiteRook1, 7, 7)
    whiteQueen = queen_moves.Queens(board, whiteQueen0, 3, 7)
    whiteKing = king_moves.Kings(board, whiteKing0, 4, 7)
    return (
        whiteAPawn, whiteBPawn, whiteCPawn, whiteDPawn, whiteEPawn, whiteFPawn, whiteGPawn, whiteHPawn, whiteBKnight,
        whiteGKnight, whiteCBishop, whiteFBishop, whiteARook, whiteHRook, whiteKing, whiteQueen)


def instantiate_black_pieces(board):
    blackAPawn = pawn_moves.Pawns(board, blackPawn0, 0, 1)
    blackBPawn = pawn_moves.Pawns(board, blackPawn1, 1, 1)
    blackCPawn = pawn_moves.Pawns(board, blackPawn2, 2, 1)
    blackDPawn = pawn_moves.Pawns(board, blackPawn3, 3, 1)
    blackEPawn = pawn_moves.Pawns(board, blackPawn4, 4, 1)
    blackFPawn = pawn_moves.Pawns(board, blackPawn5, 5, 1)
    blackGPawn = pawn_moves.Pawns(board, blackPawn6, 6, 1)
    blackHPawn = pawn_moves.Pawns(board, blackPawn7, 7, 1)
    blackBKnight = knight_moves.Knights(board, blackKnight0, 1, 0)
    blackGKnight = knight_moves.Knights(board, blackKnight1, 6, 0)
    blackCBishop = bishop_moves.Bishops(board, blackBishop0, 2, 0)
    blackFBishop = bishop_moves.Bishops(board, blackBishop1, 5, 0)
    blackARook = rook_moves.Rooks(board, blackRook0, 0, 0)
    blackHRook = rook_moves.Rooks(board, blackRook1, 7, 0)
    blackQueen = queen_moves.Queens(board, blackQueen0, 3, 0)
    blackKing = king_moves.Kings(board, blackKing0, 4, 0)
    return (
        blackAPawn, blackBPawn, blackCPawn, blackDPawn, blackEPawn, blackFPawn, blackGPawn, blackHPawn, blackBKnight,
        blackGKnight, blackCBishop, blackFBishop, blackARook, blackHRook, blackKing, blackQueen)


def put_pieces_on_board(board, white_pieces, black_pieces):
    for i in range(8):
        board[1][i] = black_pieces[i]
        board[6][i] = white_pieces[i]
    board[0][1] = black_pieces[8]
    board[0][6] = black_pieces[9]
    board[7][1] = white_pieces[8]
    board[7][6] = white_pieces[9]
    board[0][2] = black_pieces[10]
    board[0][5] = black_pieces[11]
    board[7][2] = white_pieces[10]
    board[7][5] = white_pieces[11]
    board[0][0] = black_pieces[12]
    board[0][7] = black_pieces[13]
    board[7][0] = white_pieces[12]
    board[7][7] = white_pieces[13]
    board[0][4] = black_pieces[14]
    board[7][4] = white_pieces[14]
    board[0][3] = black_pieces[15]
    board[7][3] = white_pieces[15]
