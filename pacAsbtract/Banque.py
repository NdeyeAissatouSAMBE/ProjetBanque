class Banque:
    def __init__(self, card_num):
        self.card_num = card_num

    def get_card_num(self):
        return self.card_num

    def __set__(self, card_num):
        self.numerocarte = card_num

    def verifiercarte(self, card_num):
        '''c'est une classe abstrait'''

