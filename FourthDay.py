# pattern question

# rows = int(input("Enter number of rows: "))

# start = 1

# for i in range(1, rows + 1):
    
#     curr = start
#     digsum = 0

#     print(" "*(rows-i) , end="")
#     for j in range(i):
#         print(curr, end=" ")

#         temp = curr
#         while temp !=0:
#             digsum = digsum + temp % 10
#             temp //= 10

#         curr += 1

#     print("\n")
#     start = digsum

# DICTIONARY : uniqe key, mutable

# di={1:"vedant",2:"soalnke"}
# print(di)
# print(di.values())
# print(di.keys())
# print(di.get(1))
# di1=di.copy()
# print(di1)
# di1.update({3:"Asara"})
# print(di1)
# di.clear()
# print(di)
# di1.pop(3) # pop perticular key
# print(di1)
# di1.popitem() #pop last item in dict
# print(di1)

# key=['a','b']
# dic2=dict.fromkeys('ab')
# print(dic2)
# dic2.update({'a':'vedant'})
# print(dic2)

# PATTERN

# triangale

# row=int(input("Enter no o rows="))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# row=int(input("Enter no of rows="))
# for i in range(1,row+1):
#     for j in range(row,i-1,-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#             print("*",end=" ")
#     print()

# DIAMOND

# rows=int(input("enter rows"))
# for i in range(1,rows+1):
#     for j in range(rows,i,-1):
#         print("",end=" ")
#     for k in range(1,i+1):
#          print("*",end=" ")
#     print()

# for i in range(1,rows+1):
#     for j in range(1,i+1,1):
#         print(" ",end="")
#     for k in range(rows,i,-1):
#          print("*",end=" ")
#     print()

    # FUNCTION

# start=int(input("Enter starting no ."))
# end=int(input("Enter ending no."))
# num=int(input("Enter divider"))
    
# def diff(start,end,num):
#         divsum=0
#         nondivsum=0
#         for i in range(start,end+1):
#             if i%3==0:
#                 divsum+=i
#             else:
#                 nondivsum+=i
#         diff=abs(divsum-nondivsum)
#         return diff
# print(diff(start,end,num))

## aabbbcccz= a2b3c3z

# def demo(str1):
#     str2=""
#     for i in str1:
#         if i not in str2:
#             if str1.count(i)>1:
#                 str2+=i
#                 str2+=str(str1.count(i))
#             else:
#                 str2+=i
#     print(str2)
# str1=input("Enter String :")
# demo(str1)

# ARGUMENTS

def demo(*args):
    c=0
    for i in args:
        c+=i
    return c
print(demo(12,52,31))

def demo(**kwargs): #any word after **
    print(kwargs)
print(demo(a='vedant',b='solanke'))
