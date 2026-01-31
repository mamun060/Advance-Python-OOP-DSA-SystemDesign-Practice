# Singleton Design Pattern (Python)

Singleton Design Pattern এমন একটি ডিজাইন প্যাটার্ন যা নিশ্চিত করে যে
- একটি ক্লাসের শুধুমাত্র একটি অবজেক্ট (instance) তৈরি হবে
- এবং সেই অবজেক্টটি পুরো অ্যাপ্লিকেশন জুড়ে ব্যবহার করা যাবে।

সহজ ভাষায়:
“এক ক্লাস → একটাই অবজেক্ট → সবাই শেয়ার করে ব্যবহার করবে”
---
## Singleton কী?
Singleton Design Pattern নিশ্চিত করে যে একটি ক্লাসের শুধুমাত্র একটি instance থাকবে
এবং সেই instance পুরো অ্যাপ্লিকেশন জুড়ে শেয়ার করা যাবে।

---
## কেন Singleton ব্যবহার করবো?
- Database connection শেয়ার করার জন্য
- Application configuration রাখার জন্য
- Logger বা cache manager বানানোর জন্য
---
