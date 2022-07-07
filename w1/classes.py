    def info(self):
        print("*"*80)
        print(f"fullname: {self.fullname}")
        print(f"height: {self.height")
        print(f"weight: {self.weight")
        print(f"age: {self.age}")
        print(f"shoe_size: {self.shoe_size")
        print("shoes:")
      
    
    def shoes_info(self):
        for shoe in enumerate(self.shoes):
            print("*"*80)
            print(f"Shoe number: {index + 1}")
            shoe.info()
            print("*"*80)
        return self

    def walk(self):
        distance = int(input("How far do you want to walk?"))
        print("Your Shoes...")
        self.shoes_info()
        shoe_chosen = input("What shoe do you want to walk in?")
        shoe_index = int(shoe_chosen) - 1
        
        shoe_actual = self.shoes[shoe_index]
        shoe_actual.add_km(distance)
        self.km += distance

    def get_shoes(self, shoe):
        if shoe.size != self.shoe_size:
            print("You can't have that shoe")
            return self
        self.shoes.append(shoe)
        print("You have received a new pair of shoes")
        return self

class Shoe:
    def __init__(self, brand, color, style, size):
        self.brand = brand
        self.color = color
        self.style = style
        self.size = size
        self.km = 0

    def info(self):
        print(f"brand: {self.brand}")
        print(f"color: {self.color}")
        print(f"style: {self.style}")
        print(f"size: {self.size}")
        print(f"km: {self.km}")
        return self

    def add_km(amount):
        self.km += amount
        return self

p1 = Person('Sarah', 'Somner', 142, 50, 20, 8.5)
s1 = Shoe('nike', 'green', 'low', 10)
s2 = Shoe('nike', 'green', 'low', 8.5)
s3 = Shoe('nike', 'brown', 'low', 8.5)

is_playing = True

p1.get_shoes(s2).get_shoes(s3)
while is_playing:
    if p1.km >= 150+

# p1.get_shoes(s2).get_shoes(s3)

# p1.walk()

