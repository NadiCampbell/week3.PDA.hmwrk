import unittest
from src.card import Card
from src.card_game import CardGame



class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card('Hearts', 1)
        self.card_2 = Card('Spades', 6)

        self.cards = [self.card_1, self.card_2]

    def test_check_for_ace(self):
        result = CardGame.check_for_ace(self, self.card_1)
        self.assertEqual(True, result)


    def test_highest_card(self):
        result = CardGame.highest_card(self, self.card_1, self.card_2)
        self.assertEqual(self.card_2, result)

    def test_cards_total(self):
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual('You have a total of 7', result)


