import pygame
from pygame import mixer
from checkers.config import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLUE
from checkers.game import Game
from helpers import get_row_col_from_mouse
from minimax.algorithm import minimax
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('How to play?','RULES:The opponent with the red pieces moves first.'
                                   'Pieces may only move one diagonal space forward(towards their opponents pieces)in the beginning of the game.Pieces must stay on the dark squares.'
                                   'To capture an opposing piece,jump over it by moving two diagonal spaces in the direction of the opposing piece.'
                                   'Keep in mind,the space on the other side of your opponents piece must be empty for you to capture it.'
                                   'If your piece reaches the last row on your opponent side,you may re-take one of your captured pieces and give super mario power to the piece that made it.'
                                   'There is no limit to how many Super marios a player may have.'
                                   'The first player to lose all of his or her pieces loses the game.'
                                   ' If a player is put in a position where they cannot move, they lose.'                                  
                                   ' If the players have the same amount of pieces, the player with the most double pieces wins.')

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SuperMaxio')


def main():
    pygame.mixer.init()
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while True:
        clock.tick(FPS)

        winner = game.winner()
        if winner != None:
            messagebox.showinfo("Winner", "{0}! You won smarty pants!".format("Red" if winner == (255,0,0) else "Blue"))
            break

        if game.turn == BLUE:
            value, new_board = minimax(game.get_board(), 3, BLUE, game)
            game.ai_move(new_board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(mouse_pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
