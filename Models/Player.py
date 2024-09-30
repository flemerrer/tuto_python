class Player:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon_name = pokemon.name
        self.actual_hp = pokemon.hp
        self.atkList = pokemon.attacks

    def print_hp(self):
        return str(self.actual_hp)

    def list_attack(self):
        return self.atkList