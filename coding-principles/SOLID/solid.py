# SOLID Principles Example

# Single Responsibility Principle - only one reason to change
class University:
    def __init_(self, name, location):
        self.name = name 
        self.location = location 


# Open/close principle - open for extension, closed for modification - I mean we can add new features without changeing exiting code.
class Course:
    def __init__(self, title, credits):
        self.title = title
        self.credits = credits
    
    def includeCourse(self)