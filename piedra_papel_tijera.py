player1 = input('Nombre del jugador 1: ')
player2 = input('Nombre del jugador 2: ')

while True:
    player1_choice = str(
        input((f'{player1}, que quieres jugar: piedra, papel o tijera? '))).lower()
    player2_choice = str(
        input((f'{player2}, que quieres jugar: piedra, papel o tijera? '))).lower()
    if player1_choice == 'piedra':
        if player2_choice == 'piedra':
            print('empate!')
        elif player2_choice == 'papel':
            print(f'{player2} gano!')
        elif player2_choice == 'tijera':
            print(f'{player1} gano!')

    elif player1_choice == 'papel':
        if player2_choice == 'piedra':
            print(f'{player1} gano!')
        elif player2_choice == 'papel':
            print('empate!')
        elif player2_choice == 'tijera':
            print(f'{player2} gano!')

    elif player1_choice == 'tijera':
        if player2_choice == 'piedra':
            print(f'{player2} gano!')
        elif player2_choice == 'papel':
            print(f'{player1} gano!')
        elif player2_choice == 'tijera':
            print('empate!')

    nuevo_juego = input('Quiren jugar nuvamente S/N?: ')
    if nuevo_juego.lower() == 'n':
        break
