class User:
    def __init__(self, first_name='Eric', last_name='Dang', email='email@gmail.com', age=26):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
        self.gold_card_points = 200
        print(self.gold_card_points)
        return self
    
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You do not have enough credit")
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)
        return self


person_a = User('Them')
person_a.display_info()
person_a.enroll().enroll().enroll().enroll()
person_a.spend_points(10).spend_points(30).spend_points(40).spend_points(150)