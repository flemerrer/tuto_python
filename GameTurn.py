class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.atkList = ['Charge', 'Tonnerre', 'Vivattaque']
        self.atkDmg = [20, 50, 35]

    def print_hp(self):
        return self.name + ' a ' + str(self.hp) + ' PV'

    def attack(self, cible):

        attack_choice = ''

        while not attack_choice.isdigit():

            attack_choice = self.attack_input()

            if not str(attack_choice).isdigit():
                attack_choice = ''
                print("Veuillez saisir le numéro d'une attaque valide.")

        self.attack_damage(cible, int(attack_choice))

        # p1atk = int(input('Combien de dégâts inflige ' + self.name + ' à ' + cible.name + ' ?\n'))
        # print()
        # cible.hp -= p1atk
        # msg1 = self.name + ' attaque ' + cible.name + ' qui perd ' + str(p1atk) + ' PV'
        # msg2 = cible.name + 'a maintenant ' + str(cible.hp) + ' PV'
        # maxSize = max(len(msg1), len(msg2))
        # msg1 += ' ' * (maxSize - len(msg1))
        # msg2 += ' ' * (maxSize - len(msg2))
        # cadre = '+' * (maxSize + 4)
        # print(cadre)
        # print(
        #     '+ ' + msg1 + ' +',
        #     '\n+ ' + msg2 + ' +',)
        # print(cadre + '\n')

    def attack_damage(self, cible, choix):
        ind = choix - 1
        cible.hp -= self.atkDmg[ind]
        print(self.name + ' attaque ' + cible.name + ' avec ' + self.atkList[ind] + ', qui perd ' + str(
            self.atkDmg[ind]) + ' PV.')
        print()

    def attack_input(self):
        print(self.name + ', quelle attaque voulez-vous utiliser ?\n')

        for atk in self.atkList:
            ind = self.atkList.index(atk) + 1
            print(str(ind) + '. ' + atk)

        choixAtk = input()
        print()
        return choixAtk


# p1Name = input('Entrez le nom du premier chinpokimon :').capitalize()
# p1hp = int(input('Et son nombre de points de vie :'))
# pokemon1 = Player(p1Name, p1hp)
#
# print()
#
# p2Name = input('Entrez le nom du deuxième chinpokimon :').capitalize()
# p2hp = int(input('Et son nombre de points de vie :'))
# pokemon2 = Player(p2Name, p2hp)
#
# print()

pokemon1 = Player('Pikatchoum', 100)
pokemon2 = Player('Tadpurin', 100)


def fight():
    print('\n+ ' + pokemon1.name + ' (' + str(pokemon1.hp) + ' PV) affronte ' + pokemon2.name + ' (' + str(
        pokemon2.hp) + ' PV) ' + '+\n')

    while (pokemon1.hp >= 0 and pokemon2.hp >= 0):
        attack_round()

    if (pokemon1.hp <= 0):
        declare_winner(pokemon1, pokemon2)
    elif (pokemon2.hp <= 0):
        declare_winner(pokemon2, pokemon1)


def attack_round():
    if (pokemon1.hp > 0 and pokemon2.hp > 0):
        print(pokemon1.name + ', à toi de jouer !')
        pokemon1.attack(pokemon2)

    if (pokemon1.hp > 0 and pokemon2.hp > 0):
        print(pokemon2.name + ', à toi de jouer !')
        pokemon2.attack(pokemon1)

    # result()


def result():
    msg1 = 'Résultat du round :'
    msg2 = pokemon1.print_hp()
    msg3 = pokemon2.print_hp()
    maxSize = max(len(msg2), len(msg3))
    maxSize = max(maxSize, len(msg1))
    msg1 += ' ' * (maxSize - len(msg1))
    msg2 += ' ' * (maxSize - len(msg2))
    msg3 += ' ' * (maxSize - len(msg3))
    cadre = '+' * (maxSize + 4)

    print(cadre)
    print(
        '+ ' + msg1 + ' +',
        '\n+ ' + msg2 + ' +',
        '\n+ ' + msg3 + ' +', )
    print(cadre)
    print()


def declare_winner(pkm1, pkm2):
    print(pkm1.name + ' est KO. ' + pkm2.name + ' remporte le combat ! ')
