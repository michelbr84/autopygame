import pygame
from src.settings import SETTINGS
from src.game import Game

if __name__ == "__main__":
    game = Game(SETTINGS)
    game.run()