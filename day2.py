########################FOR#################
#for i in range(1,15):
 #   print("Good morning students")
 
###################FUNCTIONS##################
#def add(a,b):
  #result=a+b
 # print(result)
#add(15,25)
#add(15,18)
################LIST##########
#students=["araftha","atesh","mercan","eylul"]
#students.append("hazar")
#students.remove("eylul")
#students.insert(1,"turkey")
#print(students)
############################tuple###############
#students=("shree","skanda","daivik")
#print(students)
####################dictionary##############
#students={"name":"Shree","usn":"1gd24cs141","sem":"5th sem","dept":"cse"}
#students["course"]="python programming"
#print(students["name"],students["usn"],students["sem"],students["dept"])




#######################CLASS AND FUNCTIONS#######################
#class student:
    #def display(self):
       # print("Hello students")
        #print("welcome to the class")
#s1=student()
#s1.display()



#################CONSTRUCTOR####################

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("marks:",self.marks)

s1 = student("shree",20,89)
s2 = student("daivik",18,90)
s1.display()
s2.display()