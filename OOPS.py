# Great Learning tutorial(Line no = 1-158)

# # Creating a class
# class Phone:
#     def set_color(self,color):
#         self.color = color

#     def set_cost(self,cost):
#         self.cost = cost

#     def show_color(self):
#         return self.color

#     def show_cost(self):
#         return self.cost        

#     def make_Call(self):
#         print("I am making a call")

#     def play_Game(self):
#         print("I am playing a game")


# p1 = Phone()      # Instantiating a p1 object

# p1.make_Call()    # Calling function
# p1.play_Game()
# p1.set_color("Red")
# p1.set_cost(50000)
# print(p1.show_color())
# print(p1.show_cost())


# Creating a class with constructor
# class Employee:
#     def __init__(self,name,age,gender,salary):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.salary = salary

#     def show_details(self):
#         print("The name of the employee is ",self.name)
#         print("The age of the employee is ",self.age)
#         print("The gender of the employee is ",self.gender)
#         print("The salary of the employee is ",self.salary)

# e1 = Employee("Saumya",25, "Female", 25000)
# e1.show_details()



# Inheritance
# Super class
# class Vehicle:
#     def __init__(self, mileage, cost):
#         self.mileage = mileage
#         self.cost = cost

#     def show_vehicle_details(self):
#         print("Mileage of vehicle is ",self.mileage)
#         print("Cost of the vehicle is ",self.cost)
#         print("I am a vehicle")

# v1 = Vehicle(500,500)
# v1.show_vehicle_details()


# Child class inheriting vehicle class
# class Car(Vehicle):
#     def show_car_details(self):
#         print("I am a Car")

# c1 = Car(250,800)
# c1.show_vehicle_details()
# c1.show_car_details()


# Overriding the init method
# class Car(Vehicle):
#     def __init__(self,mileage,cost,tyres,hp):
#         super().__init__(mileage,cost)
#         self.tyres = tyres
#         self.hp = hp

#     def show_car_details(self):
#         print("I am a car")
#         print("Number of tyres is ",self.tyres)
#         print("HorsePower is ",self.hp)


# c1 = Car(250,80000,4,100)
# c1.show_car_details()
# c1.show_vehicle_details()

# Multiple Inheritance
# class Parent1:
#     def assign_str_one(self,str1):
#         self.str1 = str1

#     def show_str_one(self):
#         return self.str1

# class Parent2:
#     def assign_str_two(self,str2):
#         self.str2 = str2

#     def show_str_two(self):
#         return self.str2

# class Child(Parent1,Parent2):
#     def assign_str_three(self,str3):
#         self.str3 = str3

#     def show_str_three(self):
#         return self.str3

# my_child = Child()

# my_child.assign_str_one("I am string of Parent 1")
# my_child.assign_str_two("I am string Parent 2")
# my_child.assign_str_three("I am string parent 3")

# print(my_child.show_str_one())
# print(my_child.show_str_two())
# print(my_child.show_str_three())

# Multilevel Inheritance

# class Parent:
#     def get_name(self,name):
#         self.name = name

#     def show_name(self):
#         return self.name

# class Child(Parent):
#     def get_age(self,age):
#         self.age = age

#     def show_age(self):
#         return self.age

# class GrandChild(Child):
#     def get_gender(self,gender):
#         self.gender = gender

#     def show_gender(self):
#         return self.gender


# gc = GrandChild()
# gc.get_name("Aayushmann")
# gc.get_age(25)
# gc.get_gender("Male")

# print(gc.show_name())
# print(gc.show_age())
# print(gc.show_gender())

# Simplilearn Tutorial OOPS concept
class Person:
    def __init__(self):
        self.name = "Ankit"
        self.age = 23
        self.gender = "Male"

    def talk(self):
        print("I am ",self.name)

    def vote(self):
        if self.age < 18:
            print("You cannot vote as your age is ",self.age)
        else:
            print("I am eligible to vote as your age is ",self.age)

p1 = Person()
p1.talk()
p1.vote()

# Polymorphism
class Car:
    def __init__(self,name):
        self.name = name

class Mercedes(Car):       # Child class
    def accelerate(self):
        print("150")

class Audi(Car):           # Child class
    def accelerate(self):
        print("200")

objL = [Audi("Audi R8"), Mercedes("Mercedes Benz")]

for obj in objL:
    print(obj.name+" : ",end="")
    obj.accelerate()
