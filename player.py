# player.py

import pygame

class Player(object):
    """docstring for Player."""

    def __init__(self, playernum):
        super(Player, self).__init__()
        self.last_button_pressed = pygame.K_ESCAPE
        self._playernum = playernum
        self._position = 0

        if self._playernum == "one":
            self.last_button_pressed = pygame.K_s
        elif self._playernum == "two":
            self.last_button_pressed = pygame.K_QUOTE

    def move(self, key):
        """moves player up"""

        if self.validForwardKeypress(key):
            self._position += 1
        return self._position
    
    @property
    def position(self):
        return self._position

    @property
    def playernum(self):
        return self._playernum

    def validForwardKeypress(self, key):
        if self._playernum == "one":
            print(self.last_button_pressed, pygame.K_s, pygame.K_a)
            if (self.last_button_pressed == pygame.K_s and key == pygame.K_a) or (
                self.last_button_pressed == pygame.K_a and key == pygame.K_s
            ):
                if self.last_button_pressed == pygame.K_a:
                    self.last_button_pressed = pygame.K_s
                else:
                    self.last_button_pressed = pygame.K_a
                return True
        elif self._playernum == "two":
            if (
                self.last_button_pressed == pygame.K_QUOTE and key == pygame.K_SEMICOLON
            ) or (
                self.last_button_pressed == pygame.K_SEMICOLON and key == pygame.K_QUOTE
            ):
                if self.last_button_pressed == pygame.K_QUOTE:
                    self.last_button_pressed = pygame.K_SEMICOLON
                else:
                    self.last_button_pressed = pygame.K_QUOTE
                return True
        return False

class MrWolf(object):
    """docstring for MrWolf."""

    def __init__(self):
        self.starttime = 0.0
        self.difficulty = 0

        self._facingforward = False

    @property
    def facingforward(self):
        return self._facingforward

    def turnaround(self):
        self._facingforward = not self._facingforward