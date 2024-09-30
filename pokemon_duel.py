# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
from Controllers import fight

if __name__ == '__main__':
    pokemon1 = pokemon_fight.select_monster('pythachu')
    pokemon2 = pokemon_fight.select_monster('pythard')

    name1 = 'Sachant'
    name2 = 'Regissseur'

    player1 = pokemon_fight.create_player(name1.upper(), pokemon1)
    player2 = pokemon_fight.create_player(name2.upper(), pokemon2)

    pokemon_fight.start(player1, player2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

