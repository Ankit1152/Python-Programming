from threading import *
from time import sleep
# Example of Single Threading done by Main Thread (which is a bydefault thread)
# Main thread runs the function one by one
# class A:
#     def run(self):
#         for i in range(5):
#             print("Class A")
#             sleep(1)

# class B:
#     def run(self):
#         for i in range(5):
#             print("Class B")
#             sleep(1)

# t1 = A()
# t2 = B()

# t1.run()
# t2.run()


# Multithreading
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Class A")
#             sleep(1)

# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("Class B")
#             sleep(1)

# t1 = A()
# t2 = B()

# # Multiple threads running simultaneously
# t1.start()
# t2.start()


# Multithreading by Telusko

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)

t1 = Hello()
t2 = Hii()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("finally print by Main thread")