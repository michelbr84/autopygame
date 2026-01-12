import pygame
import random

SHAPES = {
    'I': [[1,1,1,1]],
    'O': [[1,1],[1,1]],
    'T': [[0,1,0],[1,1,1]],
    'S': [[0,1,1],[1,1,0]],
    'Z': [[1,1,0],[0,1,1]],
    'J': [[1,0,0],[1,1,1]],
    'L': [[0,0,1],[1,1,1]],
}

def get_shape(name=None):
    if name is None:
        return random.choice(list(SHAPES.keys()))
    return SHAPES.get(name, None)

def random_shape():
    return random.choice(list(SHAPES.keys()))

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def time_to_drop(elapsed, speed):
    return elapsed > speed

def handle_input(game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.active_piece.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                game.active_piece.move(1, 0)
            elif event.key == pygame.K_UP:
                game.active_piece.rotate()
            elif event.key == pygame.K_DOWN:
                game.active_piece.move(0, 1)
            elif event.key == pygame.K_SPACE:
                game.falling = False