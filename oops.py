class Student:
    college_name="apsce"

    def __init__(self,name,marks):
       self.name=name
       self.marks=marks

    def welcome(self):
        print("welcome",self.name) 

    @staticmethod
    def hello():
        print("hello:")

s1=Student("kiran",97)
s1.welcome()
s1.hello() 
      