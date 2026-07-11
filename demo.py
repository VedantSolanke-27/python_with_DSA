#why python is called as dynamically typed language?
#math=50
#chem=60
#phy=70
#name="vedant solanke"
#print(type(math))
#print(type(chem))
#print(type(phy))
#print(type(name))

# who to check the address of any vriable? ans = id()
#print(id(math))
#print(id(chem))
#print(id(phy))
#print(id(name))

# WAP to accept a three paper marks and calculate toatal marks, percentage and display ?

#total=math+chem+phy
#percentage=total/3.0
#print("Total marks=",total)
#print("percentage=",percentage)

#what is type casting?
#ANS : convertion from one data type to another data type is type casting
#print(2+2)
#print("2"+"2") #concatenation  
#val1 = int(input("Enter first value :")) 
#val2 = int(input("Enter second value :")) 
#print(val1 + val2)
#NOTE :By default input function only accept stram value
 
#int() used to convert in integer
# print(int(3.14))
# #print(int(10+5j)) #cant
# print(int(True))
# print(int(False))
# #print(int(4.22)) #cant
# print(int("4"))

# float() used to convert
# print(float(3)) #3.0
# #print(float(2+4j)) #cant
# print(float(True))
# print(float(False))
# print(float(4.22))
# #print(float("name"))#cant
# print(float("4"))

# complex() used to convert
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# #print(complex("name")) # cant
# print(complex(5,-3))
# print(complex(True,False))

#bool() is used to convert
# print(bool(0)) #false
# print(bool(0.0)) #false
# print(bool(0+0j)) #false
# print(bool(False)) #false
# print(bool(1)) #true
# print(bool(3.14)) #true
# print(bool(1+3j)) #true
# print(bool(-1)) #true
# print(bool(True)) #true
# print(bool()) #false

#Swapping of two variables?

# val1 = int(input("Enter first value :")) 
# val2 = int(input("Enter second value :")) 
# print("before swapping :")
# print("val 1 =",val1,"  ","val 2 =",val2)
# temp=val1 #temp=100
# val1=val2 #val1=200
# val2=temp #val2=200
# print("After Swapping :")
# print("val 1 =",val1,"  ","val 2 =",val2)

# val1 = int(input("Enter first value :")) 
# val2 = int(input("Enter second value :")) 
# print("before swapping :")
# print("val 1 =",val1,"  ","val 2 =",val2)
# val1=val1+val2
# val2=val1-val2
# val1=val1-val2
# print("After Swapping :")
# print("val 1 =",val1,"  ","val 2 =",val2)

# INTREST

# principal=int(input("Enter principal amount :"))
# ROI=int(input("Enter rate of intrest :"))
# time= int(input("Enter the duration of loan amount :"))

# simple_intrest=principal*ROI*time/100
# print("simpla intrest Amount :",simple_intrest)

#AREA

# r=22
# area=3.14*r*r
# print("Area of circle :",area)

# r=22
# circumferance=2*3.14*r
# print("circumferance of circle :",circumferance)

# height=float(input("my height in feet :"))
# inch=height*12
# cm=inch*2.54
# print("my height in inch :",inch,"  ","my height in cm :",cm)

#REVERSE NO.

# num =123 #321
# a =num%10 #a=3
# num=num//10 #num=12
# b=num%10 # b=2
# c=num//10 #c=1
# rev=a*100+b*10+c #300 +20+1
# print("reverse no. :",rev)

# num=1234567
# a=num%10 #a=7
# num=num//10 #num=123456
# b=num%10 #b=6
# num=num//10 #num=12345
# c=num%10 #b=5
# num=num//10 #num=1234
# d=num%10 #b=4
# num=num//10 #num=123
# e=num%10 #b=3
# num=num//10 #num=12
# f=num%10 #b=2
# g=num//10
# rev=a*1000000+b*100000 +c*10000+d*1000+e*100+f*10+g*1
# print("reverse no. :",rev)

#identity operator: when wer want to address comparison then we should go for identity poerator ther are two type of identity operator is and is not

#MEMORY MANAGEMENT

# math =50 #same
# chem=50 #same
# phy =50 #same
# english=80 #diff
# print(id(math)) #same address
# print(id(chem)) #same address
# print(id(phy)) #same address
# print(id(english)) #diffrent address

#IDENTITY OPERATOR

# x=10 
# y=10
# z=20
# print(x is y) #true
# print(x is not y) #false
# print(y is not z) #true

#MEMBERSHIP OPERATOR : By using membership operator we check that the object is present or not in collection data structure(list,tuple,set,dict,string) 
# in = if the given object is present then it return true 
# not in = if the given object is not present then it return true 

# name="vedant"
# print('v' in name) #true
# print('s' in name) #false
# print('s' not in name) #true

#SLICING

# name="vedantsolanke"
# #indexing=0123456789 10 11 12 13
# print(name[0]) #v
# print(name[1]) #e
# print(name[-1]) #last e
# #print(name[15]) error out of range
# print(name[0:5]) #edant
# print(name[1:]) #edantsolanke
# print(name[:5]) #vedan
# print(name[:]) #vedantsolanke
# print(name[1:8:2]) #eato
# print(name[::-1]) #eknalostnadev

#CLASS

# s="help4code is a brst platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

#JOIN FUNCTION

# s="vedant","gopal","solanke"
# m='|'.join(s)
# print(m) #vedant|gopal|solanke

#CHARECTER ARRANGMENT

# s="Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

print("subject marks :")
phy=50
chem=60
math=70
print("physics={}  chemistry={}  math={}".format(phy,chem,math))
print("physics={0}  chemistry={1}  math={2}".format(phy,chem,math))
print("physics={x}  chemistry={y}  math={z}".format(x=phy,y=chem,z=math))
total=phy+chem+math
print("Total marks",f"{total}")
print("Roll No.=","7".zfill(4))