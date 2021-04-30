import pygame
import os
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLUE, CROWN
from checkers.game import Game
from checkers.algorithm.minimax import minimax
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('How to play?','RULES \n The opponent with the red pieces moves first.Pieces may only move one diagonal space forward(towards their opponents pieces)in the beginning of the game.Pieces must stay on the dark squares.To capture an opposing piece,jump over it by moving two diagonal spaces in the direction of the opposing piece.A piece may jump forward over an opponents pieces in multiple parts of the board to capture them.Keep in mind,the space on the other side of your opponents piece must be empty for you to capture it.If your piece reaches the last row on your opponent side,you may re-take one of your captured pieces and crown the piece that made it to the KingsRow.There by making it a KingPiece.Kingpieces may still only move one space at a time during an on-capturing move.However,when capturing anopponent piece(s)it may move diagonally forward or backwards.There is no limit to how many kingpieces a player may have')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    FPS = 60
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')
    pygame.mixer.init()
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == BLUE:
            value, new_board = minimax(game.get_board(), 3, BLUE, game)
            game.ai_move(new_board)

        winner = game.winner()
        if winner != None:
            Tk().wm_withdraw() #to hide the main window
            messagebox.showinfo('Winner', "you won")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(mouse_pos)
                game.select(row, col)

        game.update()

    pygame.quit()
    exit()

if __name__ == '__main__':
    main()



       
