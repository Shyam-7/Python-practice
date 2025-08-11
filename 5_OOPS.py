# Object Oriented Programming (OOP)

# Class definition
class Dog:
    # Constructor (__init__ aka special method or dunder method)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def bark(self):
        print("Woof!")

# Class instantiation
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()

# A standalone block of code aka function
def calculate_area(length, width):
    return length * width


# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, training_level):
        super().__init__(name, age)
        self.training_level = training_level

    def play(self):
        print("The puppy is playing!")

my_puppy = Puppy("Charlie", 1, "Beginner")
print(my_puppy.name)
print(my_puppy.age)
print(my_puppy.training_level)
my_puppy.bark()
my_puppy.play()

# Polymorphism
def animal_sound(animal):
    animal.bark()

animal_sound(my_dog)
animal_sound(my_puppy)

# method overriding
def bark(self):
    print("Woof! Woof!")
    super().bark()
    print("The puppy is barking!")

#method overloading
def bark(self, times=1):
    for _ in range(times):
        print("Woof!")
        super().bark()
        print("The puppy is barking!")

#method overloading
def bark(self, times=1):
    for _ in range(times):
        print("Woof!")
        super().bark()
        print("The puppy is barking!")

        


# Encapsulation
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print("Meow!")

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

my_cat = Cat("Whiskers", 2)
print(my_cat.name)
print(my_cat.get_age())
my_cat.set_age(3)
print(my_cat.get_age())

# Encapsulation in action
my_cat.set_age(4)
print(my_cat.get_age())

# Abstraction
class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        print("Flapping wings!")

    def get_info(self):
        return f"{self.name} is a {self.species}."

my_bird = Bird("Tweety", "Canary")
print(my_bird.get_info())
my_bird.fly()
