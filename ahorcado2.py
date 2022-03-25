from ast import If
import random
import string
def ahorcado(word_choice):
    ahorcadi = '''
    _____
    |    |
    |
    |
    |
    |
    '''
    print(ahorcadi + "_"*len(word_choice))
    # missing_letters = len(word_choice)
    lifes = 6
    guess_letter_list = []
    while True:
        while True:
            guess_letter = input('Ingrese una letra: ')
            if(len(guess_letter) !=1 and guess_letter.isnumeric()):
                print('Intenta poner una letra.')
            else:
                if guess_letter.lower() in guess_letter_list:
                    print('Ya intentaste con esa letra.')
                else:
                    guess_letter_list.append(guess_letter)
 
                    if guess_letter.lower() in word_choice:
                        print('¡Bien! Adivinaste una letra')
                        break
                    else:
                        lifes = lifes - 1
                        print('Error... intentalo de nuevo. Perdon pero perdiste una vida.')
                        
                        
                        if lifes == 5:
                            ahorcadi = '''
                            _____
                           |     |
                           |   (-_-)
                           |
                           |
                           |
                           '''
                           
                        elif lifes == 4:
                            ahorcadi = '''
                            _____
                           |     |
                           |   (-_-)
                           |     |
                           |     |
                           |
                           |
                           '''
                        elif lifes == 3:
                            ahorcadi = '''
                             _____
                            |     |
                            |   (-_-)
                            |    /|
                            |     |
                            |
                            |
                            '''
                        elif lifes == 2:
                            ahorcadi = '''
                             _____
                            |     |
                            |   (-_-)
                            |    /|\ 
                            |     |
                            |
                            |
                            '''
                        elif lifes == 1:
                            ahorcadi = '''
                              _____
                             |     |
                             |   (-_-)
                             |    /|\ 
                             |     |
                             |    /
                             |
                             '''
                        elif lifes == 0:
                            ahorcadi = '''
                              _____
                             |     |
                             |   (x_x)
                             |    /|\ 
                             |     |
                             |    /.\ 
                             |
                            '''
                        print("Te quedan " + str(lifes) + " vidas")
                        break
                    
        if lifes==0:
            
            print(":( Murio el ahorcado. La palabra era: "+ word_choice + ahorcadi)
            break
        status = ""
            
        missing_letters = len(word_choice)  
        for letter in word_choice:
            if letter in word_choice and letter == guess_letter:
                letter = letter
                status = status + letter
                missing_letters = missing_letters - 1
                break   
            else:
                status = status + "_" * missing_letters
                
                break
                 
        print(ahorcadi + status)

def run():
    words = ['Zeus', 'Poseidon', 'Hades', 'Hera', 'Demeter', 'Ares', 'Atenea', 'Apolo', 'Artemisa', 'Hefesto', 'Afrodita', 'Hermes', 'Dionisio', 'Iris', 'Hypnos', 'Hipnos', 'Nemesis', 'Tique', 'Tyche', 'Nike', 'Hebe', 'Hecate', 'Nyx', 'Nox', 'Thanatos', 'Tanatos', 'Eris', 'Hestia', 'Hemera', 'Forcis', 'Ceto', 'Pasitea', 'Morfeo', 'Macaria', 'Melinoe', 'Zagreus', 'Jano', 'Himeneo', 'Eros', 'Anteros', 'Fobos', 'Deimos', 'Caronte', 'Persefone', 'Anfititre', 'Triton', 'Saturno', 'Orcus', 'Belona', 'Urania', 'Caliope', 'Euterpe', 'Talia', 'Melpomene', 'Terpsicore', 'Erato', 'Polimnia', 'Asclepio', 'Quione', 'Kione', 'Eunomia', 'Dice', 'Irene', 'Carpo', 'Talo', 'Arctos', 'Selene', 'Helios', 'Calypso', 'Disnomia', 'Himero', 'Eolo', 'Cefiro', 'Apeliotes', 'Boreas', 'Notos']
    menu = ''' 
    ¡Bienvenido mi joven amigo! Hoy vamos a jugar un juego muy divertido, el ahorcado. 
    Las reglas son faciles, vos vas a ingresar letras y si son parte de la palabra que elegi van a irse sumando, ahora si no... bueno de a poco va a ir apareciendo parte por parte nuestro amigo. Si aparece todo perdiste.
    ¿Estas listo? 
    '''
    print(menu)
    start = input('Ingrese "Si" o "Por supuesto!" para iniciar. ')
    start = start.lower()
    word_choice = random.choice(words)
    word_choice = word_choice.lower()
    if start == 'si' or start == 'Por supuesto!':
        ahorcado(word_choice)

    

if __name__ == '__main__':
    run()