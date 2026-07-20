#OOPs Concept:

# Class

# class sipna:
#     a=10
#     b=20
#     def demo(self,a,b):
#         print(a,b)
# obj=sipna()
# obj.demo(50,60)
# print(obj.a)
# print(obj.b)


# class sipna:
#     a=10
#     b=20
#     def demo(self,a,b):
#         self.a=a
#         self.b=b

# obj=sipna()
# obj.demo(50,60)
# print(obj.a)
# print(obj.b)

# Constructor

# class sipna:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def demo(self):
#         print(self.a,self.b)
# obj=sipna(50,100)
# obj1=sipna(34,56)
# obj.demo()
# print(obj1.a)
# print(obj1.b)

# Inheritance

# class demo:
#     def add(self,a,b):
#         return a+b
    
# class demo1:
#     def mul(self,a,b):
#         return a*b

# class Calculator(demo,demo1):
#     def sub(self,a,b):
#         return a-b
    
# obj=demo()
# cal=Calculator()
# print(cal.add(10,20))
# print(cal.sub(50,20))
# print(cal.mul(45,5))

# class demo:
#     def add(self,a,b):
#         return a+b
    
# class demo1(demo):
#     def mul(self,a,b):
#         return a*b

# class Calculator(demo1):
#     def sub(self,a,b):
#         return a-b
    
# obj=demo()
# cal=Calculator()
# print(cal.add(10,20))
# print(cal.sub(50,20))
# print(cal.mul(45,5))


# class demo:
#     def add(self,a,b):
#         return a+b
    
# class demo1(demo):
#     def mul(self,a,b):
#         return a*b

# class Calculator(demo1):
#     def sub(self,a,b):
#         return a-b
    
# obj=demo()
# obj1=demo1()
# cal=Calculator()
# print(obj1.add(10,20))
# print(cal.sub(50,20))
# print(cal.mul(45,5))

# Encapsulation

# class sipna:
#     a=10
#     __b=20 #encapsulate
#     def demo(self): #to print b we use demo method
#         __b=20
#         print(__b)

# obj=sipna()
# print(obj.a)
# obj.demo()

#Polymorphism

# class sipna:
#     def add(self,a,b):
#         return a+b
# class sipna1(sipna):
#     def add(self,a,b,c):
#         return a+b+c
    
# obj=sipna()
# obj1=sipna1()
# print(obj.add(10,20))
# print(obj1.add(12,20,32))

# class sipna:
#     def add(self):
#         print("sipna")

# class sipna1(sipna):
#     def add(self):
#         print("sipna1")

# class sipna2(sipna1):
#     def add(self):
#         print("sipna2")

# obj=sipna()
# obj1=sipna1()
# obj2=sipna2()
# for i in obj,obj1,obj2:
#     i.add()

# 3 class list,sring,integer ever funcrtion add 
# list add tow list no 
# string concatination
# add two integer

# class integer():
#     def add(self,a,b):
#         return a+b
    
# class string(integer):
#     def add(self,a,b):
#         return a+b
    
# class list(string):
#     def add(self,a,b):
#         c=[]
#         if len(a)!=len(b):
#             return 0
#         else:
#             for i in range(len(a)):
#                 c.append(a[i]+b[i])
#                 print(c)

# obj=integer()
# obj1=string()
# obj2=list()

# print(obj.add(10,20))
# print(obj1.add("vedant","solanke"))
# obj2.add([10,20,50,60],[60,20,40,80])

# Bubble sort

# def bubble(arr,size):
#     for j in range(size):
#         print(f'pass{j}:') # for printing itteration
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="") # for printing itteration
#             print(arr) # for printing itteration
#             if(arr[i+1]<arr[i]):
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#     return arr
    
# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))

#  Optimize Bubble sort 

# def bubble(arr,size):
#     for j in range(size):
#         flag=False
#         print(f'pass{j}:') # for printing itteration
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="") # for printing itteration
#             print(arr) # for printing itteration
#             if(arr[i+1]<arr[i]):
#                 flag=True
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#         if flag==False:
#             break
#     return arr
    
# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))

# Selection sort

# def selection(arr,size):
#     for j in range(0,size-1):
#         min=j
#         for i in range(j+1,size):
#             if(arr[min]>arr[i]):
#                 min=i
#     # swapping
#         temp=arr[j]
#         arr[j]=arr[min]
#         arr[min]=temp
#     return arr
    
# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(selection(arr,size))