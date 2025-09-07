'''
By: Zoha Azam
Date: December 4, 2023
'''
import random

class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health
    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        # TODO: Implement this method.
        return f'{self.name} (health: {self.current_health}/{self.max_health})'
    
    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        # TODO: Implement this method.
        if amount > 0 and amount < self.current_health:
            self.current_health = self.current_health - amount
        if amount >= self.current_health:
            self.current_health = 0
        return self.current_health
    
    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        # TODO: Implement this method.
        alive = True
        if self.current_health > 0:
            alive = True
        if self.current_health == 0:
            alive = False
            
        return alive
    
    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        # TODO: Implement this method.
        if self.current_health != self.max_health:
            self.current_health = self.max_health      
            print(f"{self.name} has been revived!")
    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
     
        """
        # TODO: implement this method based on the attack logic above    

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    # TODO: Implement this function.
    with open(filename, 'r', encoding = "utf-8") as file: # compound statement, like: if, while, for
        list_of_lines = file.readlines()
    pokemon_stats = []
    for line in list_of_lines:
        line = line.strip()
        pokemon_stats.append(line)
    pokemon_stats = pokemon_stats[1:]
    return pokemon_stats
        
def main():
    """
    Battle of two Pokemon
    """
    pokemon_stats = read_pokemon_from_file('all_pokemon.txt')
    names = []
    attacks = []
    defenses = []
    healths = []
    for i in range(len(pokemon_stats)):
        pokemon_objects = pokemon_stats[i].split('|')
        names.append(pokemon_objects[0])
        attacks.append(pokemon_objects[1])
        defenses.append(pokemon_objects[2])
        healths.append(pokemon_objects[3])
        
    for j in range(2):     
        rand_int = random.randrange(len(pokemon_stats)-1)
        rand_num = random.randrange(len(pokemon_stats)-1)
        
    name = names[rand_int]
    attack = attacks[rand_int]
    defense = defenses[rand_int]
    health = healths[rand_int]
    
    name2 = names[rand_num]
    attack2 = attacks[rand_num]
    defense2 = defenses[rand_num]
    health2 = healths[rand_num]    
        
    pokemon1 = Pokemon(name, attack, defense, health, health)
    pokemon2 = Pokemon(name2, attack2, defense2, health2, health2)
    print(f"Welcome, {pokemon1} and {pokemon2}!")
    
main()