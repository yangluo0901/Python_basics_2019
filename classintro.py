class Animal(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print("Animal {} is eating".format(self.name))


class Dog(Animal):
    def __init__(self, name, age, color, dog_type):
        super().__init__(name, age, color)
        self.dog_type = dog_type

    def bark(self):
        print("Dog {} is barking".format(self.name))

    def eat(self):
        print("Dog {} is eating".format(self.name))


class Cat(Animal):
    def __init__(self, name, age, color, cat_type):
        super().__init__(name, age, color)
        self.cat_type = cat_type

    def lazy_sleep(self):
        print("Cat {} is lazy and sleeping".format(self.name))


def call(obj):
    obj.eat()


dog = Dog("biscuit", 8, "black", "American")
# dog.eat()
# dog.bark()
cat = Cat("cookie", 10, "white", "whatever")
animal = Animal("creature", "unknown", "yellow")
# animal.eat()
call(dog)
call(animal)

