#del Keyword use to delete object properties or object itself.
class Student:
   def __init__(self, name):
       self.name = name

s1= Student("Mobeen Khan")
print(s1.name)
del s1.name
print(s1.name)