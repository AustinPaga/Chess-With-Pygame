import check
import pygame


class Pawns:

    def __init__(self, board, piece, x, y):
        self.board = board
        self.piece = piece
        self.x = x
        self.y = y

    def set_xy(self, board):
        for a, b in enumerate(board):
            if self.piece in b:
                self.y = a
                self.x = b.index(self.piece)

    def legal_moves(self, white_pieces, black_pieces, all_pieces, board):

        pawn_legal_moves = []
        if self.piece in white_pieces:
            if self.y != 0:
                if self.x != 0 and ((board[self.y - 1][self.x - 1] in black_pieces) or (self.y == 3 and board[self.y][self.x - 1] in black_pieces and 0 <= black_pieces.index(board[self.y][self.x - 1]) < 8 and all_pieces[board[self.y][self.x - 1]][1])):
                    pawn_legal_moves.append((self.y - 1, self.x - 1))
                if self.x != 7 and ((board[self.y - 1][self.x + 1] in black_pieces) or (self.y == 3 and board[self.y][self.x + 1] in black_pieces and 0 <= black_pieces.index(board[self.y][self.x + 1]) < 8 and  all_pieces[board[self.y][self.x + 1]][1])):
                    pawn_legal_moves.append((self.y - 1, self.x + 1))
                if not board[self.y - 1][self.x]:
                    pawn_legal_moves.append((self.y - 1, self.x))
            if self.y == 6 and (not board[self.y - 2][self.x] and not board[self.y - 1][self.x]):
                pawn_legal_moves.append((self.y - 2, self.x))

        elif self.piece in black_pieces:
            if self.y != 7:
                if self.x != 0 and ((board[self.y + 1][self.x - 1] in white_pieces) or (self.y == 4 and board[self.y][self.x - 1] in white_pieces and 0 <= white_pieces.index(board[self.y][self.x - 1]) < 8 and all_pieces[board[self.y][self.x - 1]][1])):
                    pawn_legal_moves.append((self.y + 1, self.x - 1))
                if self.x != 7 and ((board[self.y + 1][self.x + 1] in white_pieces) or (self.y == 4 and board[self.y][self.x + 1] in white_pieces and 0 <= white_pieces.index(board[self.y][self.x + 1]) < 8 and all_pieces[board[self.y][self.x + 1]][1])):
                    pawn_legal_moves.append((self.y + 1, self.x + 1))
                if not board[self.y + 1][self.x]:
                    pawn_legal_moves.append((self.y + 1, self.x))
            if self.y == 1 and (not board[self.y + 2][self.x] and not board[self.y + 1][self.x]):
                pawn_legal_moves.append((self.y + 2, self.x))

        return pawn_legal_moves

    def getOutOfCheck(self, board, get_original_moves, all_pieces, white_pieces, black_pieces, white_piece_objects, black_piece_objects):
        new_moves = []

        if get_original_moves:
            for position in get_original_moves:
                # create a new board and dictionary for all the pieces to simulate with
                dummy_dict = {}
                dummy_board = [[None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None, None]]
                dummy_white_pieces = []
                dummy_black_pieces = []
                for i in all_pieces:
                    surface = pygame.Surface.copy(i)
                    dummy_dict[surface] = [all_pieces[i][0], all_pieces[i][1]]
                    for a, b in enumerate(board):
                        if i in b:
                            dummy_board[a][b.index(i)] = surface
                            break
                    if i in white_pieces:
                        dummy_white_pieces.append(surface)
                    elif i in black_pieces:
                        dummy_black_pieces.append(surface)
                self.set_xy(dummy_board)
                piece, old_y, old_x = dummy_board[self.y][self.x], self.y, self.x
                new_y, new_x = position

                # simulate en passant
                if piece in white_pieces and 0 <= white_pieces.index(piece) < 8:
                    if not dummy_board[new_y][new_x] and abs(old_y - new_y) == 1 and abs(old_x - new_x) == 1:
                        dummy_board[new_y + 1][new_x] = None

                elif piece in black_pieces and 0 <= black_pieces.index(piece) < 8:
                    if not dummy_board[new_y][new_x] and abs(old_y - new_y) == 1 and abs(old_x - new_x) == 1:
                        dummy_board[new_y - 1][new_x] = None

                # simulate captures
                dummy_board[old_y][old_x] = None
                dummy_board[new_y][new_x] = piece

                # simulate getting all the pieces' legal moves
                for key in dummy_dict:
                    dummy_dict[key][0] = []

                for key in white_piece_objects:
                    key.set_xy(board)
                    get_moves = key.legal_moves(white_pieces, black_pieces, all_pieces, board)
                    if get_moves:
                        for i in get_moves:
                            keyIndex = list(all_pieces.keys()).index(getattr(key, "piece"))
                            dummy_dict[list(dummy_dict)[keyIndex]][0].append(i)
                for key in black_piece_objects:
                    key.set_xy(board)
                    get_moves = key.legal_moves(white_pieces, black_pieces, all_pieces, board)
                    if get_moves:
                        for i in get_moves:
                            keyIndex = list(all_pieces.keys()).index(getattr(key, "piece"))
                            dummy_dict[list(dummy_dict)[keyIndex]][0].append(i)

                # check if the King is still in check after the simulation
                white_is_checked, black_is_checked, checkers = check.checkIfChecked(dummy_dict, dummy_board, dummy_white_pieces, dummy_black_pieces)

                if self.piece in white_pieces:
                    if not white_is_checked:
                        new_moves.append(position)
                elif self.piece in black_pieces:
                    if not black_is_checked:
                        new_moves.append(position)

        return new_moves



