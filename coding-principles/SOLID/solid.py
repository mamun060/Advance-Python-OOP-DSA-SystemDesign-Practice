from abc import ABC, abstractmethod
# S
class UserRepo:
    def create(self, data):
        print("User created")

class EmailService:
    def send(self, email):
        print("Email sent")

class Logger:
    def log(self, msg):
        print("Log:", msg)

# O
class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class PercentageDiscount(Discount):
    def apply(self, amount):
        return amount * 0.90

class FlatDiscount(Discount):
    def apply(self, amount):
        return amount - 100

# L
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def run(self):
        print("Running")

# I
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Robot(Workable):
    def work(self):
        print("Robot working")

class Human(Workable, Eatable):
    def work(self):
        print("Human working")
    def eat(self):
        print("Human eating")

# D
class InputDevice(ABC):
    @abstractmethod
    def press(self):
        pass

class Keyboard(InputDevice):
    def press(self):
        print("Keyboard pressed")

class Mouse(InputDevice):
    def press(self):
        print("Mouse clicked")

class Computer:
    def __init__(self, device: InputDevice):
        self.device = device

pc = Computer(Keyboard())
pc = Computer(Mouse())
