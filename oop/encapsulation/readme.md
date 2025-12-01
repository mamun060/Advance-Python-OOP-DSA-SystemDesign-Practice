# Encapsulation (ইনক্যাপসুলেশন) — Python OOP
**Encapsulation** মানে হলো **ডেটা লুকানো এবং নিয়ন্ত্রণ করা**, যাতে বাইরে থেকে সরাসরি ডেটা পরিবর্তন করা না যায়।  
Python-এ Encapsulation তিনভাবে করা যায়:

1. **Public** → সরাসরি অ্যাক্সেস করা যায়  
2. **Protected** → `_` দিয়ে শুরু, সাবক্লাসে অ্যাক্সেস করা যায়, বাইরের কোডে ব্যবহারে সতর্ক থাকা উচিত  
3. **Private** → `__` দিয়ে শুরু, বাইরের কোড সরাসরি অ্যাক্সেস করতে পারে না

---

## Python Example
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self._pin = 1234                     # Protected
        self.__balance = balance              # Private

    # Getter for private balance
    def get_balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} টাকা জমা হয়েছে।")
        else:
            print("শুধুমাত্র ধনাত্মক টাকা জমা করা যাবে।")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} টাকা উত্তোলন করা হয়েছে।")
        else:
            print("ব্যালান্স যথেষ্ট নয় বা ভুল পরিমাণ।")


# ব্যবহার
account = BankAccount("12345", 5000)

# Public variable অ্যাক্সেস
print(account.account_number)  # 12345

# Protected variable অ্যাক্সেস (সাবক্লাসে ব্যবহার করা ঠিক)
print(account._pin)            # 1234

# Private variable অ্যাক্সেস
# print(account.__balance)     # ❌ এটা কাজ করবে না

# Getter method ব্যবহার করে Private variable অ্যাক্সেস
print(account.get_balance())   # 5000

# Deposit & Withdraw
account.deposit(1500)          # 1500 টাকা জমা হয়েছে
account.withdraw(2000)         # 2000 টাকা উত্তোলন করা হয়েছে
print(account.get_balance())   # 4500
```
### Key Points (Python Context)
```
| Access Level | Syntax       | অ্যাক্সেস                                      |
| ------------ | ------------ | ---------------------------------------------|
| Public       | `self.var`   | যেকোনো জায়গা থেকে                           |
| Protected    | `self._var`  | সাবক্লাস থেকে, বাইরের কোডে সতর্কভাবে           |
| Private      | `self.__var` | শুধুমাত্র ক্লাসের ভিতরে, বাইরের কোডে সরাসরি নয় |
```
