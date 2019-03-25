from pacAsbtract.Iverificateur import Iverificateur
class Americanexpress(Iverificateur):
    '''c"est une classe qui implemente l'interface'''

    def verifiercarte(self,card_num ):
        '''c'est une methode qui permet de verifier si la carte est fiable'''
        if (str(card_num) == 17):

            '''c"est une classe qui implemente l'interface'''
            AMEX = 'Amex'
            AMEX_2 = ('39' , '30')
            '''c'est une methode qui permet de verifier si la carte est fiable'''

        if len(card_num) == 17 and card_num[:2] in AMEX_2:
                        card_type = AMEX



