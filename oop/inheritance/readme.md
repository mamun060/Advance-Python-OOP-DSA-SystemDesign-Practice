# Inheritance (ইনহেরিট্যান্স) — অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)

**Inheritance** মানে হলো "**উত্তরাধিকার / বংশগত সম্পর্ক**"।  
একটি ক্লাস অন্য ক্লাসের প্রপার্টি এবং মেথড **পায় এবং ব্যবহার করতে পারে।**  
এটি OOP-এর মূল স্তম্ভগুলোর একটি:  
**Encapsulation, Abstraction, Inheritance, Polymorphism**

---

## ইনহেরিট্যান্সের মূল ধারণা

1. **Parent Class / Base Class / Super Class**  
   - যেই ক্লাস থেকে বৈশিষ্ট্য বা মেথড নেওয়া হবে  

2. **Child Class / Derived Class / Sub Class**  
   - যেই ক্লাস Parent থেকে বৈশিষ্ট্য এবং মেথড গ্রহণ করবে  
   - চাইলে Child নিজস্ব মেথডও যোগ করতে পারে  

> ইনহেরিট্যান্স কোডকে পুনঃব্যবহারযোগ্য এবং পরিষ্কার রাখে।

---

## উদাহরণ (Python)

```python
# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} চালু হলো")

# Child Class
class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} হর্ন বাজালো!")

# Child Class
class Bike(Vehicle):
    def kickstart(self):
        print(f"{self.brand} কিকস্টার্ট হলো!")

# ব্যবহার
my_car = Car("Toyota")
my_bike = Bike("Yamaha")

my_car.start()   # Parent Class থেকে method ব্যবহার
my_car.honk()    # Child Class method

my_bike.start()  # Parent Class method
my_bike.kickstart() # Child Class method
```

### Output
```python
Toyota চালু হলো
Toyota হর্ন বাজালো!
Yamaha চালু হলো
Yamaha কিকস্টার্ট হলো!

# Child Class Car এবং Bike Parent Class Vehicle থেকে start() method পেয়েছে। এছাড়া নিজস্ব মেথডও ব্যবহার করতে পারছে।
```
### সংক্ষিপ্ত সারসংক্ষেপ
```
| বৈশিষ্ট্য    | উদাহরণ                                      |
| ------------ | ------------------------------------------- |
| Parent Class | Vehicle                                     |
| Child Class  | Car, Bike                                   |
| সুবিধা       | কোড পুনঃব্যবহারযোগ্য, সহজে maintain করা যায় |
```