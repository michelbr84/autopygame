import pygame

SHAPES = {
    'I': [[1,1,1,1]],
    'O': [[1,1],[1,1]],
    'T': [[0,1,0],[1,1,1]],
    'S': [[0,1,1],[1,1,0]],
    'Z': [[1,1,0],[0,1,1]],
    'J': [[1,0,0],[1,1,1]],
    'L': [[0,0,1],[1,1,1]],
}

COLORS = {
    'I': (0, 255, 255),
    'O': (255, 255, 0),
    'T': (128, 0, 128),
    'S': (0, 255, 0),
    'Z': (255, 0, 0),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
}

class Tetromino:
    def __init__(self, settings, shape=None, color=None):
        self.settings = settings
        self.shape = shape or utils.random_shape()
        self.color = color or utils.random_color()
        self.x = settings['BOARD_WIDTH'] // 2 - len(self.shape[0]) // 2
        self.y = 0

    def get_shape(self):
        return self.shape

    def get_color(self):
        return self.color

    def move(self, dx, dy, steps=1):
        self.x += dx * steps
        self.y += dy * steps