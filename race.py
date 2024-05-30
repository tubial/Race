"""race.py
"""

import random
import pygame
import constants
import player


class Game:
    # Mr Wolf game

    def __init__(self, goal: int, screen: pygame.Surface):
        """Game state

        Params:
            end - steps needed to win
        """
        self._playerone = player.Player("one")
        self._playertwo = player.Player("two")
        self._players = [self._playerone, self._playertwo]

        self._wolf = player.MrWolf()

        self._goal = goal

        self._sprites = pygame.sprite.Group()
        self._sprites.add(self._playerone)
        self._sprites.add(self._playertwo)
        self._sprites.add(self._wolf)

        self._screen = screen
        self._height = screen.get_height()

        # Set initial locations of the players
        self._playerone.rect.bottom = constants.HEIGHT
        self._playerone.rect.left = 0 + constants.WIDTH // 4

        self._playertwo.rect.bottom = constants.HEIGHT
        self._playertwo.rect.right = constants.WIDTH - constants.WIDTH // 4

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
    def players(self) -> list[player.Player]:
        return self._players

    def update(self, event):
        if event.key == pygame.K_s or event.key == pygame.K_a:
            self._playerone.move(event.key)
        if event.key == pygame.K_QUOTE or event.key == pygame.K_SEMICOLON:
            self._playertwo.move(event.key)

        self.playerone.rect.bottom, self.playertwo.rect.bottom = self.update_player_pos()

    def update_player_pos(self) -> list[int]:
        """Returns player's y-coords"""

        return [
            (self._height - ((item.position / self._goal) * self._height))
            for item in self.players
        ]

    def gamefinished(self):
        """returns the winning player if the game is ended
        if game is not finished, returns None"""

        if self._playerone.position >= self._goal:
            return self._playerone
        elif self._playertwo.position >= self._goal:
            return self._playertwo
        else:
            return None

    def draw(self):
        self._sprites.draw(self._screen)


def main():
    pygame.init()

    screen = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT])

    pygame.display.set_caption("Race!")

    font = pygame.font.SysFont("monotype", 20)

    done = False
    clock = pygame.time.Clock()

    game = Game(50, screen)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                game.update(event)

        screen.fill(constants.WHITE)

        game.draw()

        # Check to see if game finished
        if game.gamefinished():
            print(f"Player {game.gamefinished().playernum} wins!")
            done = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
