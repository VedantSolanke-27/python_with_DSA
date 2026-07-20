# Tree :

# from collections import deque
# class node:
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None

# class Tree:
#     def __init__(self):
#         self.root=None

#     def insert(self,data):    
#         newNode=node(data)

#         if(self.root==None):
#             self.root=newNode
#             return
#         q=deque([self.root])
#         while q:
#             temp=q.popleft()

#             if(temp.left==None):
#                 temp.left=newNode
#                 return
#             else:
#                 q.append(temp.left)
        
#             if(temp.right==None):
#                 temp.right=newNode
#                 return
#             else:
#                 q.append(temp.right)
        
#     def display(self):
#         self.inorder(self.root)

#     def bfs(self):
#         if self.root==None:
#             print("Empty")
#             return
#         q=deque([self.root])
#         while q:
#             temp=q.popleft()
#             print(temp.data,end=",")
#             if temp.left!=None:
#                 q.append(temp.left)
#             if temp.right!=None:
#                 q.append(temp.right)

#     # def dfs(self):
#     #     if self.root==None:
#     #         print("Empty")
#     #         return
#     #     s=[self.root]
#     #     while s:
#     #         temp=s.popleft()
#     #         print(temp.data,end=",")
#     #         if temp.right!=None:
#     #             s.append(temp.right)
#     #         if temp.left!=None:
#     #             s.append(temp.left)

#     def inorder(self,root):
#         if root != None :
#             self.inorder(root.left)
#             print(root.data,end=',')
#             self.inorder(root.right)
#         return

#     def preorder(self,root):
#         if root != None :
#             print(root.data,end=',')
#             self.preorder(root.left)
#             self.preorder(root.right)
#         return
    
#     def postorder(self,root):
#         if root != None :
#             self.postorder(root.left)
#             self.postorder(root.right)
#             print(root.data,end=',')
#         return
    
# t=Tree()
# t.insert(10)
# t.insert(20)
# t.insert(50)
# t.insert(30)
# t.insert(40)
# t.insert(60)
# # t.display()
# # t.inorder(t.root)
# # t.preorder(t.root)
# # t.postorder(t.root)
# # t.bfs()
# t.dfs()

# Hashing :

# dic={}
# string=input()
# for char in string:
#     if char in dic:
#         dic[char]+=1
#     else:
#         dic[char]=1
# print(dic)

# arr=[]
# for keys in dic.keys():
#     arr.append(keys)
# arr.sort()
# for keys in arr:
#     print(keys,end=":")
#     print(dic.get(keys))

# Recursion : factoria problem

def cal(num):
    if num==1:
        return num
    return num*cal(num-1)
num=int(input("Enter numbre"))
print(cal(num))