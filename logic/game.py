import random
import pygame
import time
import bishop_moves
import check
import instantiate_pieces
import king_moves
import knight_moves
import pawn_moves
import promotion
import queen_moves
import rook_moves

all_pieces = {}
white_pieces = []
white_piece_objects = []
black_pieces = []
black_piece_objects = []
captured_white_pieces = {"Pawn": 0, "Knight": 0, "Bishop": 0, "Rook": 0, "Queen": 0}
captured_black_pieces = {"Pawn": 0, "Knight": 0, "Bishop": 0, "Rook": 0, "Queen": 0}

tile_size = 32
board_pos = (200, 50)

def create_board_surf():
    board_surf = pygame.Surface((tile_size * 8, tile_size * 8))
    for boardNum in range(64):
        rect = pygame.Rect(boardNum % 8 * tile_size, boardNum // 8 * tile_size, tile_size, tile_size)
        pygame.draw.rect(board_surf, pygame.Color("grey" if (boardNum % 2 == 1 and boardNum // 8 % 2 == 1) or (boardNum % 2 == 0 and boardNum // 8 % 2 == 0) else "white"), rect)
    return board_surf

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(board_pos)
    x, y = [int(v // tile_size) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0:
            return board[y][x], y, x
    except IndexError:
        pass
    return None, None, None

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)
    return board

def draw_pieces(game_display, board):
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece:
                pos = pygame.Rect(board_pos[0] + x * tile_size - 1, board_pos[1] + y * tile_size - 1, tile_size,
                                  tile_size)
                game_display.blit(piece, piece.get_rect(center=pos.center).move(1, 1))

def drag(game_display, board, selected_piece):
    if selected_piece:
        try:
            piece, y, x = selected_piece
            if x is not None:
                rect = (board_pos[0] + x * tile_size, board_pos[1] + y * tile_size, tile_size, tile_size)
                pygame.draw.rect(game_display, (0, 255, 0, 50), rect, 2)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            game_display.blit(piece, piece.get_rect(center=pos))
            selected_rect = pygame.Rect(board_pos[0] + selected_piece[2] * tile_size, board_pos[1] + selected_piece[1] * tile_size, tile_size, tile_size)
            pygame.draw.line(game_display, pygame.Color('red'), selected_rect.center, pos)
            y, x = get_square_under_mouse(board)[1], get_square_under_mouse(board)[2]
        except TypeError:
            y, x = selected_piece[1], selected_piece[2]
        return y, x

def list_white_and_black_pieces(board):
    for i in instantiate_pieces.instantiate_white_pieces(board):
        white_piece_objects.append(i)
        white_pieces.append(getattr(i, "piece"))
        all_pieces[getattr(i, "piece")] = [[], False]
    for i in instantiate_pieces.instantiate_black_pieces(board):
        black_piece_objects.append(i)
        black_pieces.append(getattr(i, "piece"))
        all_pieces[getattr(i, "piece")] = [[], False]

def list_all_legal_moves(board):
    for key in all_pieces:
        all_pieces[key][0] = []
    for key in white_piece_objects:
        skip = True
        for a, b in enumerate(board):
            if getattr(key, "piece") in b:
                skip = False
                break
        if skip:
            continue
        key.set_xy(board)
        get_original_moves = key.legal_moves(white_pieces, black_pieces, all_pieces, board)
        get_moves = key.getOutOfCheck(board, get_original_moves, all_pieces, white_pieces, black_pieces, white_piece_objects, black_piece_objects)
        if get_moves:
            all_pieces[getattr(key, "piece")][0] = get_moves
    for key in black_piece_objects:
        skip = True
        for a, b in enumerate(board):
            if getattr(key, "piece") in b:
                skip = False
                break
        if skip:
            continue
        key.set_xy(board)
        get_original_moves = key.legal_moves(white_pieces, black_pieces, all_pieces, board)
        get_moves = key.getOutOfCheck(board, get_original_moves, all_pieces, white_pieces, black_pieces, white_piece_objects, black_piece_objects)
        if get_moves:
            all_pieces[getattr(key, "piece")][0] = get_moves

def en_passant(piece, board, new_y, new_x, old_y, old_x):
    if piece in white_pieces and 0 <= white_pieces.index(piece) < 8:
        if not board[new_y][new_x] and abs(old_y - new_y) == 1 and abs(old_x - new_x) == 1:
            board[new_y + 1][new_x] = None
    elif piece in black_pieces and 0 <= black_pieces.index(piece) < 8:
        if not board[new_y][new_x] and abs(old_y - new_y) == 1 and abs(old_x - new_x) == 1:
            board[new_y - 1][new_x] = None
    for i in range(8):
        all_pieces[white_pieces[i]][1] = False
    if piece in white_pieces and 0 <= white_pieces.index(piece) < 8:
        if abs(old_y - new_y) == 2:
            all_pieces[piece][1] = True
        else:
            all_pieces[piece][1] = False
    elif piece in black_pieces and 0 <= black_pieces.index(piece) < 8:
        if abs(old_y - new_y) == 2:
            all_pieces[piece][1] = True
        else:
            all_pieces[piece][1] = False

def castles(piece, board, new_y, new_x, old_y, old_x):
    if piece == instantiate_pieces.blackKing0 or piece == instantiate_pieces.whiteKing0:
        if new_x - old_x == 2:
            board[new_y][new_x - 1] = board[new_y][new_x + 1]
            board[new_y][new_x + 1] = None
        elif new_x - old_x == -2:
            board[new_y][new_x + 1] = board[new_y][new_x - 2]
            board[new_y][new_x - 2] = None

def pawn_promotion(board):
    for i in range(8):
        for h in range(8):
            if board[0][i] == white_pieces[h]:
                print("promoted")
                promotion.instantiate_promoted_pieces("white", "queen", all_pieces, white_pieces, black_pieces, white_piece_objects, black_piece_objects, board, 0, i)
            elif board[7][i] == black_pieces[h]:
                promotion.instantiate_promoted_pieces("black", "queen", all_pieces, white_pieces, black_pieces, white_piece_objects, black_piece_objects, board, 7, i)

def move_and_capture(board, drop_pos, selected_piece):
    piece, old_y, old_x = selected_piece
    new_y, new_x = drop_pos
    en_passant(piece, board, new_y, new_x, old_y, old_x)
    castles(piece, board, new_y, new_x, old_y, old_x)
    if board[new_y][new_x] and board[new_y][new_x] in black_pieces:
        if isinstance(black_piece_objects[black_pieces.index(board[new_y][new_x])], pawn_moves.Pawns):
            captured_black_pieces["Pawn"] += 1
        elif isinstance(black_piece_objects[black_pieces.index(board[new_y][new_x])], knight_moves.Knights):
            captured_black_pieces["Knight"] += 1
        elif isinstance(black_piece_objects[black_pieces.index(board[new_y][new_x])], bishop_moves.Bishops):
            captured_black_pieces["Bishop"] += 1
        elif isinstance(black_piece_objects[black_pieces.index(board[new_y][new_x])], rook_moves.Rooks):
            captured_black_pieces["Rook"] += 1
        elif isinstance(black_piece_objects[black_pieces.index(board[new_y][new_x])], queen_moves.Queens):
            captured_black_pieces["Queen"] += 1
    elif board[new_y][new_x] and board[new_y][new_x] in white_pieces:
        if isinstance(white_piece_objects[white_pieces.index(board[new_y][new_x])], pawn_moves.Pawns):
            captured_white_pieces["Pawn"] += 1
        elif isinstance(white_piece_objects[white_pieces.index(board[new_y][new_x])], knight_moves.Knights):
            captured_white_pieces["Knight"] += 1
        elif isinstance(white_piece_objects[white_pieces.index(board[new_y][new_x])], bishop_moves.Bishops):
            captured_white_pieces["Bishop"] += 1
        elif isinstance(white_piece_objects[white_pieces.index(board[new_y][new_x])], rook_moves.Rooks):
            captured_white_pieces["Rook"] += 1
        elif isinstance(white_piece_objects[white_pieces.index(board[new_y][new_x])], queen_moves.Queens):
            captured_white_pieces["Queen"] += 1
    board[old_y][old_x] = None
    board[new_y][new_x] = piece

    pawn_promotion(board)
    if (piece in black_pieces and 12 <= black_pieces.index(piece) <= 14) or (piece in white_pieces and 12 <= white_pieces.index(piece) <= 14):
        all_pieces[piece][1] = True

def white_computer_turn(board):
    pick_again = True
    while pick_again:
        selected_piece = None
        continue_loop = True
        piece = random.choice(white_pieces)
        for a, b in enumerate(board):
            if piece in b:
                selected_piece = piece, a, b.index(piece)
                continue_loop = False
                break
        if continue_loop:
            continue
        if all_pieces[piece][0]:
            target_square = random.choice(all_pieces[piece][0])
            drop_pos = target_square[0], target_square[1]
            move_and_capture(board, drop_pos, selected_piece)
            list_all_legal_moves(board)
            pick_again = False

def has_white_won(board):
    winner = False
    bk_checked = False
    bk_no_moves_left = True
    black_is_stalemated = False
    y, x = None, None

    for a, b in enumerate(board):
        if instantiate_pieces.blackKing0 in b:
            y, x = a, b.index(instantiate_pieces.blackKing0)
    for i in black_pieces:
        if all_pieces[i][0]:
            bk_no_moves_left = False
            break
    for i in white_pieces:
        if all_pieces[i][0]:
            if (y, x) in all_pieces[i][0]:
                bk_checked = True
    if bk_no_moves_left and bk_checked:
        winner = True
    elif bk_no_moves_left:
        black_is_stalemated = True
    return winner, black_is_stalemated


def black_computer_turn(board):
    pick_again = True
    while pick_again:
        selected_piece = None
        continue_loop = True
        piece = random.choice(black_pieces)
        for a, b in enumerate(board):
            if piece in b:
                selected_piece = piece, a, b.index(piece)
                continue_loop = False
                break
        if continue_loop:
            pass
        elif all_pieces[piece][0]:
            target_square = random.choice(all_pieces[piece][0])
            drop_pos = target_square[0], target_square[1]
            move_and_capture(board, drop_pos, selected_piece)
            list_all_legal_moves(board)
            pick_again = False

def has_black_won(board):
    winner = False
    wh_is_checked = False
    wh_no_moves_left = True
    white_is_stalemated = False
    y, x = None, None

    for a, b in enumerate(board):
        if instantiate_pieces.whiteKing0 in b:
            y, x = a, b.index(instantiate_pieces.whiteKing0)
    for i in white_pieces:
        if all_pieces[i][0]:
            wh_no_moves_left = False
            break
    for i in black_pieces:
        if all_pieces[i][0]:
            if (y, x) in all_pieces[i][0]:
                wh_is_checked = True
    if wh_no_moves_left and wh_is_checked:
        winner = True
    elif wh_no_moves_left:
        white_is_stalemated = True
    return winner, white_is_stalemated

def update_board(board, gameDisplay, board_surf, clock):
    gameDisplay.fill(pygame.Color("grey"))
    gameDisplay.blit(board_surf, board_pos)
    draw_pieces(gameDisplay, board)
    pygame.display.flip()
    clock.tick(60)
    time.sleep(0)

def white_user_click(gameDisplay, board, selected_piece, drop_pos, board_surf, clock):
    not_moved = True
    while not_moved:
        piece, y, x = get_square_under_mouse(board)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and piece is not None and piece in white_pieces:
                selected_piece = piece, y, x
            elif event.type == pygame.MOUSEBUTTONUP and drop_pos and selected_piece:
                if all_pieces[selected_piece[0]][0] and drop_pos in all_pieces[selected_piece[0]][0]:
                    move_and_capture(board, drop_pos, selected_piece)
                    not_moved = False
                    list_all_legal_moves(board)
                    break
                selected_piece = None
                drop_pos = None
        gameDisplay.fill(pygame.Color("grey"))
        gameDisplay.blit(board_surf, board_pos)
        draw_pieces(gameDisplay, board)
        # update_board(board, gameDisplay, board_surf, clock, board_pos)
        drop_pos = drag(gameDisplay, board, selected_piece)
        pygame.display.flip()
        clock.tick(60)

def black_user_click(gameDisplay, board, selected_piece, drop_pos, board_surf, clock):
    not_moved = True
    while not_moved:
        piece, y, x = get_square_under_mouse(board)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and piece is not None and piece in black_pieces:
                selected_piece = piece, y, x
            elif event.type == pygame.MOUSEBUTTONUP and drop_pos and selected_piece:
                if all_pieces[selected_piece[0]][0] and drop_pos in all_pieces[selected_piece[0]][0]:
                    move_and_capture(board, drop_pos, selected_piece)
                    not_moved = False
                    list_all_legal_moves(board)
                    break
                selected_piece = None
                drop_pos = None
        gameDisplay.fill(pygame.Color("grey"))
        gameDisplay.blit(board_surf, board_pos)
        draw_pieces(gameDisplay, board)
        # update_board(board, gameDisplay, board_surf, clock, board_pos)
        drop_pos = drag(gameDisplay, board, selected_piece)
        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((640, 480))
    board = create_board()
    board_surf = create_board_surf()
    pygame.display.set_caption("Chess Game")
    clock = pygame.time.Clock()
    list_white_and_black_pieces(board)
    instantiate_pieces.put_pieces_on_board(board, white_pieces, black_pieces)
    list_all_legal_moves(board)
    black_wins = False
    white_wins = False
    white_is_stalemated = False
    black_is_stalemated = False
    update_board(board, gameDisplay, board_surf, clock)
    selected_piece = None
    drop_pos = None
    while not black_wins and not white_wins and not black_is_stalemated and not white_is_stalemated:
        # white_computer_turn(board)
        white_user_click(gameDisplay, board, selected_piece, drop_pos, board_surf, clock)
        print("Captured black pieces: ", captured_black_pieces)
        white_wins, black_is_stalemated = has_white_won(board)
        update_board(board, gameDisplay, board_surf, clock)
        if not white_wins and not black_is_stalemated:
            # black_computer_turn(board)
            black_user_click(gameDisplay, board, selected_piece, drop_pos, board_surf, clock)
            print("Captured white pieces: ", captured_white_pieces)
            black_wins, white_is_stalemated = has_black_won(board)
            update_board(board, gameDisplay, board_surf, clock)
    if white_is_stalemated or black_is_stalemated:
        print("Stalemate")
    elif white_wins:
        print("White is Victorious!")
    elif black_wins:
        print("Black is Victorious!")

if __name__ == "__main__":
    main()
