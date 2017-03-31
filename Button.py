''' A class for a button object '''

import pygame
from Vector2 import Vector2

class Button(object):
    ''' Class for button object '''
    def __init__(self, valx, valy, text):
        self.position = Vector2(valx, valy)
        self.text = text
        