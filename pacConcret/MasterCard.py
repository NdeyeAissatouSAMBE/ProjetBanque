from pacAsbtract.Iverificateur import Iverificateur
class MASTERCARD(Iverificateur):

    '''c"est une classe qui implemente l'interface'''
    MASTERCARD = 'MasterCard'
    MASTERCARD_2 = ('40', '41')

    def verifiercarte(self, card_num):
        '''c'est une methode qui permet de verifier si la carte est fiable'''
        if len(card_num) == 16:


            # MasterCard
            if len(card_num) == 16 and card_num[:2] in MASTERCARD_2 :
                card_type = MASTERCARD

