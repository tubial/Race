"""race.py
"""
import random
import pygame
import constants
import player


class Game(object):
    # docstring for Game

    def __init__(self, end):
        """Game state

        Arguments:
        end - steps needed to win
        """
        self._playerone = player.Player("one")
        self._playertwo = player.Player("two")

        self._wolf = player.MrWolf()

        self._stepsend = end

    @property
    def get_playerone(self):
        return self._playerone

    @property
    def get_playertwo(self):
        return self._playertwo

    def gamefinished(self):
        """returns the winning player if the game is ended
        if game is not finished, returns None"""

        if self._playerone.position >= self._stepsend:
            return self._playerone
        elif self._playertwo.position >= self._stepsend:
            return self._playertwo
        else:
            return None
        
def main():
    game = Game(10)

    pygame.init()

    screen = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT])

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
                    game.get_playerone.move(event.key)
                if event.key == pygame.K_QUOTE or event.key == pygame.K_SEMICOLON:
                    game.get_playertwo.move(event.key)

        screen.fill(constants.WHITE)

        screen.blit(font.render(str(game.get_playerone.position), 1, constants.BLACK, constants.WHITE), (5, 5))
        screen.blit(font.render(str(game.get_playertwo.position), 1, constants.BLACK, constants.WHITE), (5, 50))

        # Check to see if game finished
        if game.gamefinished():
            print(f"Player {game.gamefinished().playernum} wins!")
            done = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
