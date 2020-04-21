# Python object review

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# for in loops
# for key in object:

for attribute in dojo:
    print(attribute)
    print(dojo[attribute])
    # continue looping through lists

# Class syntax
# attributes and methods

class User():
    def __init__(self, name, w_name, attack):
        self.name = name
        self.warrior_type = Warrior(w_name, attack)
        self.hp = 100
    # print all user attributes
    def status(self):
        print(f"User is {self.name}, they're a {self.warrior_type} and have {self.hp} HP.")
        return self
    # prints a greeting between users
    def sayHello(self, another_user):
        print(f"{self.name} says hello to {another_user.name}")
        return self


# print(tobin.name, raj.name, tobin.warrior_type, raj.warrior_type, tobin.hp, raj.hp)
# tobin.status().status().name

# Creating instances
# the self

tobin = User("Tobin", "ninja", 15)
print(tobin.name, tobin.warrior_type.name)

raj = User("Raj", "knight", 20)

# Affecting other class instances

# tobin.sayHello(raj).attack(raj)
# raj.attack(tobin).status()
# tobin.status()

# Inheritance


class Warrior():
    def __init__(self, name, attack):
        self.name = name
        self.attack_p = attack
    def attack(self, target):
        print(f"{self.name} has attacked {target.name}!")
        if self.name == 'ninja':
            print(f"{self.name} used a shuriken! Attack did 10 Damage!")
            target.hp -= 10
        elif self.name == 'knight':
            print(f"{self.name} takes a slash with their sword! Attack does 15 damage!")
            target.hp -= 15
        return self

tobin.warrior_type.attack(raj)