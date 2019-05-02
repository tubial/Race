import unittest
import race
import pygame

class MyTest(unittest.TestCase):
    def testvalidkeypressplayerone(self):
        player = race.Player("one")
        player.last_button_pressed = pygame.K_a

        self.assertEqual(player.validForwardKeypress(pygame.K_s), True)
        self.assertEqual(player.validForwardKeypress(pygame.K_a), True)

    def testvalidkeypressplayertwo(self):
        player = race.Player("two")
        player.last_button_pressed = pygame.K_QUOTE

        self.assertEqual(player.validForwardKeypress(pygame.K_SEMICOLON), True)
        self.assertEqual(player.validForwardKeypress(pygame.K_QUOTE), True)

    def testmove(self):
        player = race.Player("one")
        player.move

        player.last_button_pressed = pygame.K_a

        self.assertEqual(player.move(pygame.K_s), 1)
        self.assertEqual(player.move(pygame.K_a), 2)

    def testturnaround(self):
        mrwolf = race.MrWolf()

        # self.assertEqual()

if __name__ == '__main__':
    unittest.main()