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

**একটি ক্লাসের শুধু একটি কাজ থাকবে।  
একটি ক্লাসকে একাধিক দায়িত্ব দেওয়া যাবে না।**

### সহজভাবে:
“একজন মানুষ এক কাজ করলেই ভালো হয়।”

### খারাপ উদাহরণ:
একটি ক্লাসের কাজ:
- ডেটা সেভ করা  
- ইমেইল পাঠানো  
- ইনভয়েস প্রিন্ট করা  

➡ সব একসাথে মিশে গেছে — SRP ভঙ্গ।

### ভালো উদাহরণ:
- **User** → শুধু ডেটা রাখবে  
- **EmailService** → শুধু ইমেইল পাঠাবে  
- **InvoicePrinter** → শুধু ইনভয়েস প্রিন্ট করবে  

**ফায়দা:** কোড পরিষ্কার, পরিবর্তন করা সহজ।

---

## O — Open/Closed Principle (OCP)

**কোড পরিবর্তন না করে নতুন ফিচার যোগ করা যাবে।**  
“Open for extension, closed for modification.”

### সহজভাবে:
নতুন কিছু যোগ করতে চাইলে পুরনো কোড ছুঁতে যাবে না।

### উদাহরণ (Discount System):
নতুন ডিসকাউন্ট যোগ করতে হলে:

- `PercentageDiscount`  
- `FixedDiscount`  
- `NewYearDiscount` (নতুন)

➡ পুরনো কোড পরিবর্তন করতে হয় না।  
সবকিছু *extension* এর মাধ্যমে হয়।

---

## L — Liskov Substitution Principle (LSP)

**Child ক্লাস Parent ক্লাসের জায়গায় ব্যবহার করলেও কোনো সমস্যা হওয়া যাবে না।**

### সহজভাবে:
“বাবার জায়গায় ছেলে বসলেও কাজ চালু থাকতে হবে।”

### উদাহরণ:
যেখানে `DiscountStrategy` দরকার, সেখানে তুমি ব্যবহার করতে পারো—

- `PercentageDiscount`  
- `FixedDiscount`  
- `NoDiscount`  

➡ সিস্টেম ভাঙবে না — এটিই LSP।

---

## I — Interface Segregation Principle (ISP)

**বড় Interface না বানিয়ে, ছোট ছোট প্রয়োজন অনুযায়ী Interface ব্যবহার করবে।**

### সহজভাবে:
“একজনকে এমন কাজ দিতে যাবে না, যেটা সে করতে পারে না।”

### খারাপ উদাহরণ:
একটি Interface:

Robot → `eat()` করতে পারে না।  
➡ সমস্যার সৃষ্টি।

### ভালো সমাধান:
- `Workable`  
- `Eatable`  

যে যা পারে, সেটাই implement করবে।
---

## D — Dependency Inversion Principle (DIP)

**High-level এবং Low-level উভয়ই abstraction-এর ওপর নির্ভর করবে।**

### সহজভাবে:
“মানুষ সরাসরি ড্রাইভার নয়, গাড়ির ইন্টারফেসের ওপর ভরসা করে।”

### উদাহরণ:
`InvoicePrinter` সরাসরি:

`PercentageDiscount` বা `FixedDiscount` চেনে না।

বরং—

✔ এটি শুধু `DiscountStrategy` (abstraction) চেনে।  
তাই যেকোনো ডিসকাউন্ট ক্লাস ব্যবহার করা যায়।
---



