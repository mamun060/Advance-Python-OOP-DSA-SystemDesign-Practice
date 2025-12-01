# Polymorphism (পলিমরফিজম) — অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)

**Polymorphism** মানে হলো "**অনেক রূপ**"।  
একই মেথড বা ফাংশন বিভিন্ন ক্লাসে **ভিন্নভাবে কাজ করতে পারে**।  
এটি OOP-এর চারটি মূল স্তম্ভের একটি:  

---

## Types of Polymorphism

1. **Run-time Polymorphism (Method Overriding)**  
   - চাইল্ড ক্লাসে প্যারেন্ট ক্লাসের মেথডের নিজস্ব ইমপ্লিমেন্টেশন করা  
   - রানটাইমে কাজ করে

2. **Compile-time Polymorphism (Method Overloading)**  
   - একই নামের মেথড, কিন্তু প্যারামিটার আলাদা  
   - কম্পাইল টাইমে ঠিক হয়  

> নোট: Python-এ সরাসরি Overloading নেই, তবে ডিফল্ট আর্গুমেন্ট ব্যবহার করে করা যায়।

---

## উদাহরণ (Python)

### 1️- Run-time Polymorphism (Method Overriding)

```python
class Animal:
    def speak(self):
        print("Animal শব্দ করে")

class Dog(Animal):
    def speak(self):
        print("Dog বলে Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat বলে Meow!")

# পলিমরফিজম ব্যবহার
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()

# output 
Dog বলে Woof!
Cat বলে Meow!
Animal শব্দ করে
```
### 2️- Compile-time Polymorphism (Method Overloading এর সিমুলেশন Python-এ)
```python
class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))      # আউটপুট: 5
print(m.add(2, 3, 4))   # আউটপুট: 9
```
---
```
| বৈশিষ্ট্য                 | উদাহরণ                                    |
| ------------------------- | ----------------------------------------- |
| Run-time Polymorphism     | Dog/Cat ক্লাসে `speak()` ওভাররাইড করা     |
| Compile-time Polymorphism | `add()` মেথডের ডিফল্ট প্যারামিটার ব্যবহার |
| সুবিধা                    | একই ইন্টারফেস, ভিন্ন আচরণ                 |
```
---
