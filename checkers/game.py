import pygame
from .board import Board
from .config import RED, WHITE, BLUE, BLACK, SQUARE_SIZE


class Game():
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            return True

        return False

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            half_square_size = SQUARE_SIZE // 2
            x_pos = col * SQUARE_SIZE + half_square_size
            y_pos = row * SQUARE_SIZE + half_square_size
            radius = 15
            pygame.draw.circle(self.win, BLUE, (x_pos, y_pos), radius)

    def change_turn(self):
        self.valid_moves = {}
        self.turn = BLUE if self.turn == RED else RED

    def winner(self):
        return self.board.winner(self.turn)

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
