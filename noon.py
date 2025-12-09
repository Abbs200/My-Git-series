class Student:
    def __init__ (self, name, major, GPA, is_on_probation):
      self.name= name
      self.GPA=GPA
      self.major=major
      
    def honor(self):
        if self.GPA >= 3.5:
          return 'On honor roll'
        else:
           return 'U embarassement'
    
    
first_stud= Student('jim', 'medicine', 3.2, False)
secon_stud= Student('alex', 'medicine', 3.8, True)

print(first_stud)  # <__main__.Student object at 0x000001CDD3236A50>
# tells u it's object & the location of memory stored in

print(first_stud.name)  # jim

print(Student)  # <class '__main__.Student'> 

print(first_stud.__init__())  # U embarassement

 
