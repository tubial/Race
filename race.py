"""race.py
"""

import random
import pygame
import constants
import player


class Game:
    # docstring for Game

    def __init__(self, end):
        """Game state

        Arguments:
        end - steps needed to win
        """
        self._playerone = player.Player("one")
        self._playertwo = player.Player("two")
        self._players = [[self._playerone, 0], [self._playertwo, 0]]

        self._wolf = player.MrWolf()

        self._goal = end

        self._sprites = pygame.sprite.Group()
        self._sprites.add(self._playerone)
        self._sprites.add(self._playertwo)
        self._sprites.add(self._wolf)

    @property
    def playerone(self) -> player.Player:
        return self._playerone

    @property
    def playertwo(self) -> player.Player:
        return self._playertwo

    @property
    def mrwolf(self):
        return self._wolf

    @property
    def players(self):
        return self._players

    def update(self, event):
        if event.key == pygame.K_s or event.key == pygame.K_a:
            self._playerone.move(event.key)
        if event.key == pygame.K_QUOTE or event.key == pygame.K_SEMICOLON:
            self._playertwo.move(event.key)

    def player_status(self):
        """status of players

        returns:
            list of players and percentages to finish
        """
        # update player's progress
        for pl in self._players:
            pl[1] = pl[0].position / self._goal

        return self._players

    def gamefinished(self):
        """returns the winning player if the game is ended
        if game is not finished, returns None"""

        if self._playerone.position >= self._goal:
            return self._playerone
        elif self._playertwo.position >= self._goal:
            return self._playertwo
        else:
            return None

    def draw(self, screen):
        self._sprites.draw(screen)


def main():
    game = Game(100)

    pygame.init()

    screen = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT])

    pygame.display.set_caption("Race!")

    font = pygame.font.SysFont("monotype", 20)

    done = False
    clock = pygame.time.Clock()

    # Set initial location of players
    game.playerone.rect.bottom  = constants.HEIGHT
    game.playerone.rect.left = 0

    game.playertwo.rect.bottom = constants.HEIGHT
    game.playertwo.rect.right = constants.WIDTH

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                game.update(event)

        screen.fill(constants.WHITE)

        game.draw(screen)

        for n, pl in enumerate(game.player_status()):
            screen.blit(
                font.render(str(pl[1]), 1, constants.BLACK, constants.WHITE),
                (5, 5 * n * 10),
            )

        # Check to see if game finished
        if game.gamefinished():
            print(f"Player {game.gamefinished().playernum} wins!")
            done = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
