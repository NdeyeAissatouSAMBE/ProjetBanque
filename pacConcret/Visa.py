from pacAsbtract.Iverificateur import Iverificateur
class Visaverifier(Iverificateur):
        '''c"est une classe qui implemente l'interface'''
        def verifiercarte(self,card_num):
            '''c'est une methode qui permet de verifier si la carte est fiable'''
            if(str(card_num)==15):
                ''
            if (str(card_num) == 17):
                '''c"est une classe qui implemente l'interface'''
                VISA = 'Visa'
                VISA_2 = ('14', '15')
                '''c'est une methode qui permet de verifier si la carte est fiable'''

            if len(card_num) == 17 and card_num[:2] in VISA_2:
                card_type = VISA