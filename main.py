"""
Crear minijuego de piedra, papel o tijera cumpliendo con los siguientes enunciados:
1. Reglas del juego:
    - Piedra gana a tijera
    - Tijera gana a papel
    - Papel gana a piedra
    - El minijuego es multijugador y el equipo juega el papel del oponente y elige un elemento aleatorio de la lista de elementos
2. Interacción con el usuario:
    - La consola se usa para interactuar con el jugador.
    - El jugador puede elegir una de las tres opciones: rock, paper o scissors.
    - El jugador puede elegir si vuelve a jugar.
    - Se debe advertir al jugador si introduce una opción no válida.
    - El jugador ve su puntuación al final del juego.
3. Validación de la entrada de usuario:
    - En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
    - El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.
    - Al final de cada ronda, el jugador debe responder si quiere jugar de nuevo o no.
"""
import random
import os
import time

# Funciones
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    # Variables
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    playing = True

    # Inicio del juego
    clear()
    print('Welcome to Rock, Paper, Scissors!\n')
    player_name = input('Please, enter your name: ')
    print(f'\nHello {player_name.capitalize()}, let\'s play!\n')
    time.sleep(1)

    while playing:
        # Elección del jugador
        print('\nChoose your option:\n')
        for option in options:
            print(f' - {option.capitalize()}')
        player_choice = input('\nWhat do you choose?: ').lower()
        while player_choice not in options:
            print(f'\n{player_choice} is not a valid option.')
            player_choice = input('What do you choose?: ').lower()

        # Elección de la computadora
        computer_choice = random.choice(options)
        print(f'The computer chose: {computer_choice.capitalize()}')

        # Resultados
        if player_choice == computer_choice:
            print('\nIt\'s a tie!')
        elif player_choice == 'rock':
            if computer_choice == 'scissors':
                print('\nYou win!')
                player_score += 1
            else:
                print('\nYou lose!')
                computer_score += 1
        elif player_choice == 'paper':
            if computer_choice == 'rock':
                print('\nYou win!')
                player_score += 1
            else:
                print('\nYou lose!')
                computer_score += 1
        elif player_choice == 'scissors':
            if computer_choice == 'paper':
                print('\nYou win!')
                player_score += 1
            else:
                print('\nYou lose!')
                computer_score += 1

        # Puntuación
        print(f'\n{player_name.capitalize()}, your score is: {player_score}')
        print(f'The computer score is: {computer_score}')

        # Repetir
        play_again = input('\nDo you want to play again? (y/n): ').lower()
        while play_again not in ('y', 'n'):
            print(f'\n{play_again} is not a valid option.')
            play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again == 'n':
            playing = False
            print('\nThanks for playing!')
            time.sleep(1)
            clear()
        else:
            clear()
            print('Let\'s play again!\n')
            time.sleep(1)  

# Inicio del programa
if __name__ == '__main__':
    game()

# Fin del programa