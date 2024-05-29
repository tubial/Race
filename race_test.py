import unittest
import player
import pygame


class MyTest(unittest.TestCase):
    def testvalidkeypressplayerone(self):
        some_player = player.Player("one")
        some_player.last_button_pressed = pygame.K_a

        self.assertEqual(some_player.validForwardKeypress(pygame.K_s), True)
        self.assertEqual(some_player.validForwardKeypress(pygame.K_a), True)

    def testvalidkeypressplayertwo(self):
        some_player = player.Player("two")
        some_player.last_button_pressed = pygame.K_QUOTE

        self.assertEqual(some_player.validForwardKeypress(pygame.K_SEMICOLON), True)
        self.assertEqual(some_player.validForwardKeypress(pygame.K_QUOTE), True)

    def testmove(self):
        some_player = player.Player("one")

        some_player.last_button_pressed = pygame.K_a

        self.assertEqual(some_player.move(pygame.K_s), 1)
        self.assertEqual(some_player.move(pygame.K_a), 2)

    def testturnaround(self):
        mrwolf = player.MrWolf()

        # self.assertEqual()


if __name__ == "__main__":
    unittest.main()
