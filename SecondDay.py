#CONDITIONAL STATMENT

#IF STATEMENT

# age=int(input("age of the person="))
# if (age>=18):
#     print("person is eligibal for vote")
# else:
#     print("person is not eligibal for vote")

#ELIF STATEMENT

# num1=int(input("first no is ="))
# num2=int(input("second no is ="))
# num3=int(input("Third no is ="))

# if num1>num2 and num1>num3:
#     print("num1 is gretest")
# elif num2>num1 and num2>num3:
#     print("num2 is gretest")
# else:
#     print("num3 is gretest")

#LOOPs

#FOR LOOP

# list1=[10,345,'vedant',34.5] #store hetrogenious data
# for i in list1:
#     print(i)
# for i in range(1,5):
#     print(i)
# for i in range(1,5+1):
#     print(i)
# for i in range(1,5+1,2):
#     print(i)

# list1=[12,10,18,63,61,17,25,29,91,56]
# evenCount=oddCount=0
# for i in list1:
#     if i%2==0:
#         evenCount+=1 # evencount=evencount+1
#     else:
#         oddCount+=1 #oddCount=oddCount+1
# print("even=",{evenCount})
# print("odd=",{oddCount})

# RVERSE No. WITH WHILE LOOP

# num=int(input("enter the no="))
# rev=0
# while num!=0: #suppose 532
#     rev=rev*10+num%10 #first cycle : 0*10+2, SC:2*10+3, TC: 23*10+5
#     num=num//10 # num=53 , num=5 , num=0
# print(rev)

#PALENDROM

# num=int(input("Enter the number="))
# temp=num
# rev=0
# while num!=0:
#     rev=rev*10+num%10
#     num=num//10
# if temp==rev:
#     print("given no is palendrom")
# else:
#     print("given no is not palendrom")

#DIGIT SUM

# num=int(input("Enter no."))
# sum=0
# while num!=0:
#     sum=sum+num%10 # OR sum+=num%10
#     num=num//10
# print(sum)

#FACTORIAL

# num=int(input("Enter any no."))
# fact=1
# for i in range (2,num+1):
#     fact=fact*i
# print(fact)

#FABBONASSIS SERIES :

# num=int(input("Enter any no."))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(2,num):
#     c=a+b # FIRST CYCLE c=1, SC c=2....
#     print(c,end=",")
#     a=b #a=1, a=1,....
#     b=c #b=1, b=2,....

# ARMSTRONG NO : no which addition of each digit to the power of total count of digit in no. is equal to given no
#EX>  153=1^3+5^3+3^3=153

num=int(input("Enter NO."))
temp=num
count=len(str(num))
sum=0
while num!=0:
    sum+=(num%10)**count
    num//=10 # num=num//10
if temp==sum:
    print("IT is ARMSTRONG NO")
else:
    print("IT IS NOT ARMSTRONG NO")
