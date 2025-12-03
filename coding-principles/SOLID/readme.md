## SOLID Principles (Object-Oriented Design)

The **SOLID** principles are a set of five design guidelines that help developers write clean, maintainable, scalable, and flexible code. They are essential for Low-Level Design (LLD).

---

### 1. **S — Single Responsibility Principle (SRP)**  
A class should have **only one reason to change**.  
It should focus on **one job or responsibility**.

✔ Makes classes smaller and easier to understand  
✔ Reduces bugs and side effects  

---

### 2. **O — Open/Closed Principle (OCP)**  
Software entities (classes, modules, functions) should be:  
- **Open for extension**  
- **Closed for modification**

Meaning you can add new features **without modifying existing code**, usually through abstraction (interfaces, inheritance).

---

### 3. **L — Liskov Substitution Principle (LSP)**  
Subclasses should be usable **in place of their parent class** without breaking the system.  

✔ Ensures correct inheritance  
✔ Avoids unexpected behavior  

If `Child` replaces `Parent`, the program should still work correctly.

---

### 4. **I — Interface Segregation Principle (ISP)**  
Clients should not be forced to depend on **interfaces they do not use**.  

Break large interfaces into **smaller, specific** ones.

✔ Avoids bloated interfaces  
✔ Keeps classes clean and focused  

---

### 5. **D — Dependency Inversion Principle (DIP)**  
High-level modules should not depend on low-level modules.  
Both should depend on **abstractions**.

✔ Increases flexibility  
✔ Makes code easier to test  
✔ Promotes loose coupling  

---

### Summary Table

| Principle | Meaning |
|----------|---------|
| SRP | One class = One responsibility |
| OCP | Extend behavior without modifying existing code |
| LSP | Subclasses must behave like their base class |
| ISP | Prefer many small interfaces over one large interface |
| DIP | Depend on abstractions, not concrete implementations |

---

# SOLID Principles — বাংলায় সহজ ব্যাখ্যা

SOLID হলো ৫টি গুরুত্বপূর্ণ ডিজাইন প্রিন্সিপল, যা কোডকে পরিষ্কার, মেইনটেইনেবল এবং স্কেলেবল করতে সাহায্য করে। নিচে প্রতিটি প্রিন্সিপল বাংলায় সহজভাবে ব্যাখ্যা করা হলো।

---

## S — Single Responsibility Principle (SRP)

**একটি ক্লাসের শুধু একটি কাজ থাকবে। একটি ক্লাসকে একাধিক দায়িত্ব দেওয়া যাবে না।**

### সহজভাবে:
“একজন মানুষ এক কাজ করলেই ভালো হয়।”

### example
```python
class UserService:
    def create_user(self, data):
        print("User created")

    def send_email(self, email):
        print("Sending welcome email")

    def log(self, message):
        print("Log:", message)

**ফায়দা:** কোড পরিষ্কার, পরিবর্তন করা সহজ।
```
### Key Difference
| উদাহরণ                                        | Class responsibility | SRP Status | ব্যাখ্যা                    |
| --------------------------------------------- | -------------------- | ---------- | --------------------------- |
| User CRUD + Email + Logging                   | Multiple unrelated   | ❌ Bad      | একাধিক reason to change     |
| UserService: create/update/delete             | User Management      | ✔ Good     | এক responsibility           |
| OrderService + DiscountService + EmailService | Each class one area  | ✔ Good     | এক responsibility per class |

### Summary 
* এক class → এক reason to change
* SRP = “Reason to Change” principle
* Multiple related functions → allowed
* Multiple unrelated functions → SRP break
---

## O — Open/Closed Principle (OCP)

**কোড পরিবর্তন না করে নতুন ফিচার যোগ করা যাবে। মানে সিস্টেম নতুন feature এর জন্য open, কিন্তু modify করার জন্য closed থাকবে**  
“Open for extension, closed for modification.”

### সহজভাবে:
নতুন কিছু যোগ করতে চাইলে করতে পারবা তবে পুরনো কোড ছুঁতে যাবে না।

### example (Discount System):
```python
from abc import ABC, abstractmethod

# ai discount interface tai sobai use korbe but change korbena
class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

# Preview discount interface ta use kore new features create korbe
class PercentageDiscount(Discount):
    def apply(self, amount):
        return amount * 0.90

class FlatDiscount(Discount):
    def apply(self, amount):
        return amount - 100

# নতুন Discount → শুধু নতুন class
```
---
## L — Liskov Substitution Principle (LSP)

**Child ক্লাস Parent ক্লাসের জায়গায় ব্যবহার করলেও কোনো সমস্যা হওয়া যাবে না। মানে Child class parent-এর জায়গায় বসতে পারবে সিস্টেম না ভেঙে।**

### সহজভাবে:
“বাবার জায়গায় ছেলে বসলেও কাজ চালু থাকতে হবে।”

### example 
```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def run(self):
        print("Running")
```
➡ Behavior separate করা হলো।

---

## I — Interface Segregation Principle (ISP)

**বড় Interface না বানিয়ে, ছোট ছোট প্রয়োজন অনুযায়ী Interface ব্যবহার করবে। মানে বড় interface → ভেঙে ছোট ছোট interface বানাতে হবে।**

### সহজভাবে:
“একজনকে এমন কাজ দিতে যাবে না, যেটা সে করতে পারে না।”

### example
```python
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
```
---
## D — Dependency Inversion Principle (DIP)

**High-level এবং Low-level উভয়ই abstraction-এর ওপর নির্ভর করবে।**

### সহজভাবে:
“মানুষ সরাসরি ড্রাইভার নয়, গাড়ির ইন্টারফেসের ওপর ভরসা করে।”

### example
```python 
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
```



