#Queue
# Type of Queue 1.Linear  2.Circular 3.Priority  4.Double Ended 
# defaut value is front =-1 and rear = -1

# class QueueIm:
#     def __init__(self):
#         self.front=-1
#         self.rear=-1
#         self.size=5
#         self.queue=[0]*self.size
    
#     def Enqueue(self,data):
#         if self.rear==self.size-1:
#             print("OverFlow")
#         elif self.front==-1 and self.rear==-1:
#             self.front+=1
#             self.rear+=1
#             self.queue[self.rear]=data
#         else:
#             self.rear+=1
#             self.queue[self.rear]=data

#     def Dequeue(self):
#         if self.front==self.size:
#             print("UnderFlow")
#         else:
#             print(f'{self.queue[self.front]} item dequeue')
#             self.front+=1

#     def Display(self):
#         for i in range(self.front,self.rear+1):
#             print(self.queue[i],end=",")






# choice=1
# qu=QueueIm()
# while choice!=0:
#     print("1. Enqueue")
#     print("2. Dequeue")
#     print("3. Dispaly")
#     choice=int(input())
#     if choice==1:
#         data=int(input("Enter data"))
#         qu.Enqueue(data)
#     elif choice==2:
#         qu.Dequeue()
#     elif choice==3:
#         qu.Display()

# Searching:
# linear search : O(n)

# def linearsearch(arr,key):
#     for i in range(0,len(arr)):
#         if arr[i]==key:
#             return i
#     return -1
    
# li=[8,5,1,9,75,15,45,63,20,10,17]
# key=int(input("Enter key value"))
# result=linearsearch(li,key)
# if(result==-1):
#     print("key not found")
# else:
#     print(f'key found at {result+1}')


# binaary search :O(logn)

# def Binarysearch(arr,key,low,high):
#         if low<=high:
#             mid=(low+high)//2
#             if(arr[mid]<key):
#                 return Binarysearch(arr,key,mid+1,high)

#             elif(arr[mid]>key):
#                 return Binarysearch(arr,key,low,mid-1)
#             else:
#                 return mid
    



# li=[2,3,6,15,20,25,28,42,48,79,88,99,100]
# key=int(input("Enter key value"))
# result=Binarysearch(li,key,0,len(li)-1)
# if(result==None):
#     print("key not found")
# else:
#     print(f'key found at {result+1}')

# Game: Guess the number

# import random as rd

# num=rd.randint(1,100)
# chances=10
# while chances>0:
#     chioce=int(input("Guess the number:"))
#     if chioce<num:
#         print(f'you guess too low!! you have only {chances} available')
#     elif chioce>num:
#         print(f'you guess too high!! you have only {chances} available')
#     else:
#         print("Congratulation !!!!! bro")
#         break
#     chances-=1

# Binary Tree: node at most have two chilldren
# type: 1. full bt 2. complete bt 3. perfect bt 4. degerated bt


# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.data = data
#         self.right = None


# class Tree:
#     def __init__(self):
#         self.root = None

#     def createNode(self, data):
#         newNode = Node(data)
#         self.insert(newNode)

#     def insert(self, newNode):
#         if self.root is None:
#             self.root = newNode
#             return

#         queue = [self.root]

#         while queue:
#             temp = queue.pop(0)

#             if temp.left is None:
#                 temp.left = newNode
#                 return
#             else:
#                 queue.append(temp.left)

#             if temp.right is None:
#                 temp.right = newNode
#                 return
#             else:
#                 queue.append(temp.right)

#     def display(self):
#         self.inorder(self.root)

#     def inorder(self, root):
#         if root is not None:
#             self.inorder(root.left)
#             print(root.data, end=" ")
#             self.inorder(root.right)


# # Driver Code
# t = Tree()

# t.createNode(10)
# t.createNode(20)
# t.createNode(30)
# t.createNode(40)
# t.createNode(50)

# print("Inorder Traversal:")
# t.display()