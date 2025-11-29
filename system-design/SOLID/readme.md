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

