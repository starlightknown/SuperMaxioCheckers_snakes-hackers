from copy import deepcopy  
from checkers.config import RED, BLUE
import pygame

#checks till last node / winner 
def minimax(board, depth, max_player, game):
    if depth == 0 or board.winner(BLUE if max_player else RED) != None:
        return board.evaluate(), board

    best_move = None
    if max_player:
        max_eval = float('-inf') #max_player maximizes, worst case -infinity
        for move in get_all_moves(board, BLUE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf') #worst case +infinity
        for move in get_all_moves(board, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):  
    moves = []  #ai adds moves to the list

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def draw_moves(game, board, piece):  
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5 )
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()

