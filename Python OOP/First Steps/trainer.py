from pokemon import Pokemon
class Trainer:
    def __init__(self,name:str):
        self.name = name
        self.pokemons = list()

    def add_pokemon(self,pokemon: Pokemon):
        if pokemon.pokemon_name in self.pokemons:
            return 'This pokemon is already caught'
        self.pokemons.append(pokemon.pokemon_name)
        return f'Caught {pokemon.pokemon_name} with health {pokemon.pokemon_health}'

    def release_pokemon(self,pokemon_name: str):
        print(self.pokemons)
        self.pokemon_name = pokemon_name
        if self.pokemon_name in self.pokemons:
            self.pokemons.remove(self.pokemon_name)
            return f'You have released {self.pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        res = f'Pokemon Trainer {self.name}\n'
        res += f'Pokemon count {len(self.pokemons)}\n'
        res += ''.join([f'- {Pokemon(p,100).pokemon_details()}\n' for p in self.pokemons])
        return res


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())