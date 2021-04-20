import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLUE, CROWN
from checkers.game import Game
from checkers.minimax.algorithm import minimax
from pygame import mixer

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
        if game.winner() != None:
            print(game.winner())
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
    pygame.quit()

if __name__ == '__main__':
    main()

       
