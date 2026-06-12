# PYTHON OOPs

# Create a class Car with a method drive() that prints "Car is moving". Create an object of Car and call drive()
class Car:
    def drive(self):
        print("Car is moving")

obj=Car()
obj.drive()



# Create a class Person with a constructor ( __init__ ) that accepts name and age as arguments and stores them as instance attributes.
    # Create an object and print the person’s name and age
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Person's name is {self.name} and age is {self.age}.")
obj=Person("Avneesh", 30)
obj.info()



# Create a base class Animal with a method sound() that prints "Some sound" .
    # Create a derived class Dog that overrides sound() to print "Bark!".
    # Create an object of Dog and call sound().
class Animal():
    def sound(self):
        print("Some sound")    
class Dog(Animal):
    def sound(self):
        print("Bark")
obj=Dog()
obj.sound()