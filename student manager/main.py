#class student:
 #   def __init__(self,usn,name,marks):
  #      self.usn=usn
   #     self.name=name
    #    self.marks=marks

    #def display(self):
     #   print("USN:",self.usn)
      #  print("Name:",self.name)
       # print("Marks:",self.marks)
        #print("-------------")

#class StudentManagement:
 #   def __init__(self):
  #      self.students=[]

#    def add_student(self):
 #       usn=input("Enter USN:")

  #      for student in self.students:
   #         if student.usn==usn:
    #            print("USN already exists")
     #           return
      #  name=input("Enter the name of the students:")
       # marks=float(input("Enter the marks:"))
        #new_student=student(usn,name,marks)
        #self.students.append(new_student)
        #print("Student added successfully")

    #def view_student(self):
     #   if len(self.students)==0:
      #      print("No student found")
       #     return

        #for student in self.students:
         #   student.display()

#    def search_student(self):
 #       usn=input("Enter USN to search:")

#        for student in self.students:
 #           if student.usn==usn:
  #              print("Student found")
   #             student.display()
    #            return
     #   print("Student not found")
#
 #     for student in self.students:
  #          if student.usn==usn:
   #            print("Student deleted")
    #            return
     #   print("Student not found")
#app=StudentManagement()

#while True:
#    print("\n#######Student  Management  System##########")
 #    print("1. Add student")
  #   print("2. View student")
   #  print("3. search student")
    # print("4. delete student")
     #print("5. exit")

     #choice=input("Enter your choice:")

     #if choice=="1":
      #   app.add_student()
     #elif choice=="2":
      #   app.view_student()
     #elif choice=="3":
      #   app.search_student()
     #elif choice=="4":
      #   app.delete_student()
     #elif choice=="5":
      #   print("thank you for using the application")
       #  break
     #else:
        # print("Invalid choice!Try again")
########################ENCAPSULATION###############
#class student:
    #def __init__(self):
     #   self.__marks=0
    #def set_marks(self,marks):
   #       print("Student marks:",self.__marks)
#s1=student()
#s1.set_marks(85.5)
#s1.show_marks()

######################INHERITANCE###################
# class grandfather:
#     def house(self):
#         print("grandfather has a house")

# class father(grandfather):
#     def car(self):
#         print("Father has a car")
# class son(father):
#     def bike(self):
#         print("Son has a bike")
# s=son()
# s.house()
# s.car()
# s.bike()

#################HEIRARCHY################

# class father:
#     def car(self):
#         print("Father has a car")
# class son(father):
#     def car(self):
#         print("Son has a car")
# class daughter(father):
#     def car(self):
#         print("Daughter has a car")
# f=father()
# s=son()
# d=daughter()
# f.car()
# s.car()
# d.car()


####################POLYMORPHISM##############
# class animal:
#     def sound(self):
#         print("animal makes a sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class cat(animal):
#     def sound(self):
#         print("cat meows") 
# animals=[dog(),cat(),animal()]
# for animal in animals:
#     animal.sound() 

######################ABSTRACT###################

#from abc import ABC,abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
# class UPI(payment):
#     def pay(self,amount):
#         print(f"Paid{amount}using UPI")
# class card(payment):
#     def pay(self,amount):
#         print(f"Paid{amount}using card")
# p1=UPI()
# p2=card()
# p1.pay(100)
# p2.pay(200)
      