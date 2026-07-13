# DATA TYPES:

#LIST: Mutsble,Orderd ,Hetrogeniousand Duplicate

# list=[19,54,76,'vedant',13.75]
# #print(list)
# list.append('sipna')
# print(list)
# list.remove(76)
# #print(list)
# list.reverse()
# #print(list)
# #print(len(list))
# list.append(19)
# print(list.count(19))

list1=[23,545,65,67,34]

# list2=list.copy()
# #print(list2)
# list2.clear()
# print(list2)

# list1.sort()
# print(list1)
# list1.pop(1)
# print(list1)

# print(list1.index(545))

# list1.extend(['vedant','solanke'])
# print(list1)

# newlist=[[323,45,65],[56,66,45]]
# # print(newlist)
# for i in newlist:
#     for j in i:
#         print(j,end=",")

#  Remove duplicate element from a list take list by user

# list=[]
# size=int(input("enter sizze of list"))
# for i in range(0,size):
#     list.append(int(input("Enter Element")))
# print(list)
# for i in list:
#     while list.count(i)>1:
#         list.remove(i)
# print(list)

# TUPLE: Imutable,Orderd,

# tuple=(10,20,30,40)
# # print(tuple)
# # print(tuple[2])
# print(tuple.count(10))
# print(tuple.index(30))

# org=[]
# size=int(input("Enter size of array"))
# for i in range(0,size):
#     org.append(int(input()))
# even=[]
# odd=[]
# even.append(org[0])
# for i in range(1,size):
#     if i%2!=0:
#         even.append(org[i])
#     else:
#         odd.append(org[i])
# even.sort()
# odd.sort()
# print("second largest element=",{even[len(even)-2]})
# print("second smallest element=",{odd[1]})

# SET : Unique,Imutable,unorderd

s={10,52,84,45}
s1={10,52,84,45,26,34,25}
s.add(34)
print(s.union(s1))
s.issubset(s1)
s1.issuperset(s)
s3=s1.copy()
print(s)
print(s3)
