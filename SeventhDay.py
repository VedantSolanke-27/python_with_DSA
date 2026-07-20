# Stack: first in last out/ last in first out deafault empty stack top-1

# class stack:
#     size=5
#     top=-1
#     stack=[]

# def overflow(self):
#     if(self.top==self.size-1):
#         return True
#     return False

# def underflow(self):
#     if(self.top==-1):
#         return True
#     return False

# def push(self,data):
#     if(self.Overflow()):
#         print("overflow!!")
#     else:
#         top+=1
#         self.stack[self.top]=data

# def pop(self):
#     if(self.underflow()):
#         print("Undeerflow!!")
#     else:
#         self.top-=1

# def display(self):
#     for i in range(self.top,-1,-1):
#         print(self.stack[i])

# s=stack()
# choice=1
# while choice!=0:
#     print("1. push()")
#     print("2. pop()")
#     print("2. display()")
#     if (choice==1):
#         data=int(input("Enter your data"))
#         push(data)
#     elif(choice==2):
#         pop()   
#     elif(choice==3):
#         display()

