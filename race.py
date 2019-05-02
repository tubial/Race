"""
 Race.py
 Tim Ubial
 7 December 2017
 Version 0.1
"""
import random
import pygame

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 600
HEIGHT = 800


class Player(object):
    """docstring for Player."""

    def __init__(self, playernum):
        super(Player, self).__init__()
        self.last_button_pressed = pygame.K_ESCAPE
        self.playernum = playernum
        self._position = 0

        if self.playernum == "one":
            self.last_button_pressed = pygame.K_s
        elif self.playernum == "two":
            self.last_button_pressed = pygame.K_QUOTE

    def move(self, key):
        """moves player up"""

        if self.validForwardKeypress(key):
            self._position += 1
        return self._position
    
    @property
    def position(self):
        return self._position

    def validForwardKeypress(self, key):
        if self.playernum == "one":
            if (self.last_button_pressed == pygame.K_s and key == pygame.K_a) or (
                self.last_button_pressed == pygame.K_a and key == pygame.K_s
            ):
                if self.last_button_pressed == pygame.K_a:
                    self.last_button_pressed = pygame.K_s
                else:
                    self.last_button_pressed = pygame.K_a
                return True
        elif self.playernum == "two":
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
        super(MrWolf, self).__init__()

        self.starttime = 0.0
        self.difficulty = 0

        self.facingforward = False

    def turnaround(self):
        facingforward is not facingforward

class Game(object):
    # docstring for Game

    def __init__(self, end):
        """Game state

        Arguments:
        end - steps needed to win
        """
        self._playerone = Player("one")
        self._playertwo = Player("two")
        self._stepsend = end
    
    @property
    def end(self):
        return self._end

    def gamefinished(self):
        """returns the winning player if the game is ended
        if game is not finished, returns None"""

        if self._playerone.position > self._stepsend:
            return self._playerone
        elif self._playertwo.position > self._stepsend:
            return self._playertwo
        else:
            return None
        
def main():
    game = Game()

    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    pygame.display.set_caption("Race!")

    font = pygame.font.SysFont("monotype", 20)

    done = False
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_a:
                    playerone.move(event.key)
                if event.key == pygame.K_QUOTE or event.key == pygame.K_SEMICOLON:
                    playertwo.move(event.key)

        screen.fill(WHITE)

        screen.blit(font.render(str(playerone.position), 1, BLACK, WHITE), (5, 5))
        screen.blit(font.render(str(playertwo.position), 1, BLACK, WHITE), (5, 50))

        # Check to see if game finished
        if game

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
