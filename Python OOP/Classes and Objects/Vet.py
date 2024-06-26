from typing import List


class Vet:
    animals: List[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name):
        self.animal_name = animal_name
        if len(Vet.animals) >= Vet.space:
            return "Not enough space"
        Vet.animals.append(self.animal_name)
        self.animals.append(self.animal_name)
        return f"{self.animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)}. {Vet.space - len(Vet.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
