from singleton import Singleton

obj1 = Singleton("First Instance")
obj2 = Singleton("Second Instance")

print(obj1.value)  # Output: First Instance
print(obj2.value)  # Output: First Instance