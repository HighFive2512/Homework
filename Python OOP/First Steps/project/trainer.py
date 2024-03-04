from project.pokemon import Pokemon
from typing import List
class Trainer:
    def __init__(self,name:str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self,pokemon: Pokemon):
        if pokemon in self.pokemons:
            return 'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self,pokemon_name: str):
        try:
            pokemon = next(filter(lambda p : p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return 'Pokemon is not caught'
        self.pokemons.remove(pokemon)
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        res = f'Pokemon Trainer {self.name}\n'
        res += f'Pokemon count {len(self.pokemons)}\n'
        res += '\n'.join([f'- {p.pokemon_details()}' for p in self.pokemons])
        return res
