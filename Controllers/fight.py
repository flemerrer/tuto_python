from random import randrange

from Models.Monster import Monster
from Models.Player import Player

monsters = {
    'pythachu': {
        'name': 'Pythachu',
        'attacks': ['tonnerre', 'charge', 'nuke'],
    },
    'pythard': {
        'name': 'Pythard',
        'attacks': ['jet-de-flotte', 'charge'],
    },
    'ponytha': {
        'name': 'Ponytha',
        'attacks': ['brûlure', 'charge'],
    },
}

attacks_damage = {
    'charge': 20,
    'tonnerre': 50,
    'jet-de-flotte': 40,
    'brûlure': 40,
    'nuke':100
}


def select_monster(pokemon_name):
    monster = Monster(
        monsters.get(pokemon_name, {'name': 'NA'})['name'],
        monsters.get(pokemon_name, {'attacks': 'NA'})['attacks']
    )
    return monster


def create_player(player_name, selected_pokemon):
    player = Player(player_name, selected_pokemon)
    return player


def start(player1, player2):
    print(f'\n{player1.name} a choisi {player1.pokemon_name} ({player1.actual_hp} PV) pour affronter '
          f'{player2.name} et son {player2.pokemon_name} ({player2.actual_hp} PV)\n')

    while player1.actual_hp > 0 and player2.actual_hp > 0:
        player_turn(player1, player2)
        player_turn(player2, player1)

    declare_winner(player1, player2)


def player_turn(player, target):
    if player.actual_hp > 0 and target.actual_hp > 0:
        print(f'{player.pokemon_name}, à toi de jouer ! Il reste {target.actual_hp} PV à {target.pokemon_name}')
        print(player.name + f', quelle attaque voulez-vous utiliser avec {player.pokemon_name} ?\n')

        index = -1

        while index == -1:

            for atk in player.atkList:
                print(f'{player.atkList.index(atk) + 1}. {atk}')

            attack_choice = input('> ')
            attack_number = len(player.atkList)

            if str(attack_choice).isdigit():
                index = int(attack_choice) - 1
                if index >= attack_number or index < 0:
                    index = -1
                    print("Veuillez saisir le nom ou numéro d'une attaque valide.")
            else:
                if attack_choice in player.atkList:
                    index = player.atkList.index(attack_choice)
                else:
                    index = -1
                    print("Veuillez saisir le nom ou numéro d'une attaque valide.")

        damage = attacks_damage.get(player.atkList[index])
        target.actual_hp -= damage

        print(f'\n{player.name} attaque {target.name} avec {player.atkList[index]}, qui perd {str(damage)} PV.\n')


def result(winner, loser):
    msg1 = f'{loser.pokemon_name} est KO. {winner.name} remporte le combat ! '
    msg2 = f'{winner.pokemon_name} gagne {randrange(20, 99)} EXP.'
    max_size = max(len(msg1), len(msg2))
    msg1 += ' ' * (max_size - len(msg1))
    msg2 += ' ' * (max_size - len(msg2))
    cadre = '+' * (max_size + 4)

    print(cadre)
    print(f'+ {msg1} +', f'\n+ {msg2} +')
    print(cadre)


def declare_winner(player1, player2):
    if player1.actual_hp > player2.actual_hp:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1

    result(winner, loser)