from pet_class import Pet
class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

pet1 = Pet('Bob', 'cow', 'run')
ninja1 = Ninja('Haiya', 'Oooo', pet1, 'corn', 'grass')
ninja1.walk()
ninja1.feed()
ninja1.bathe()