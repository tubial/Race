# player.py

import pygame
import random
import constants


class Player(pygame.sprite.Sprite):
    """Player"""

    def __init__(self, playernum):
        super().__init__()

        self.last_button_pressed = pygame.K_ESCAPE
        self._playernum = playernum
        self._position = 0

        self.image = pygame.Surface([10, 10])

        self.rect = self.image.get_rect()

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


class MrWolf(pygame.sprite.Sprite):
    """docstring for MrWolf."""

    last_turn = 0

    def __init__(self):
        super().__init__()

        self.difficulty = 0

        self.image = pygame.Surface((constants.WIDTH, 10))
        self.image.fill(constants.RED)

        self.rect = self.image.get_rect()

        self.facingforward = False

        self._next_turn = random.randrange(2, 8)

    def update(self):
        """Updates the wolf to be facing forward after a random amount of time."""
        if self.facingforward:
            pass
        else:
            if pygame.time.get_ticks() - self.last_turn >= self._next_turn:
                self.facingforward = True

                self._next_turn = random.randrange(2, 8)
