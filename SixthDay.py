# # Insertion Sort

# # algorithm
# for i in range(1,size):
#     temp=arr[i]
#     j=i-1
#     while j>=0 AND temp<=arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#     #After while loop
#     arr[j+1]=temp

# i 
# # 1 2 3 4 5 j=

# # 5 2 3 6 0 1 
# # 5 5 3 6 0 1
# # 2 5 3 6 0 1 
# # 2 5 5 6 0 1
# # 2 3 5 6 0 1 
# # 2 3 5 5 0 1 
# # 2 3 5 6 0 1 
# # 2 3 5 6 6 1
# # 2 3 5 5 6 1
# # 2 3 3 5 6 1
# # 2 2 3 5 6 1
# # 0 2 3 5 6 1 
# # 0 2 3 5 6 1
# # 0 2 3 5 6 6 
# # 0 2 3 5 5 6
# # 0 2 3 3 5 6 
# # 0 2 2 3 5 6
# # 0 1 2 3 5 6



# def insertion(arr,size):
#     for i in range(1,size):
#         temp=arr[i]
#         j=i-1
#         while j>=0 and temp<=arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=temp
#     return arr

# size=int(input())
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(insertion(arr,size))


# consonants and vowels

# alpa=str(input("Enter the string"))
# vcount=0
# ccount=0
# vowels="aeiouAEIOU"
# for i in alpa:
#     if i not in vowels:
#         ccount+=1
#     else:
#         vcount+=1
# print("Its is Consonants count",ccount)
# print("It is Vowels count",vcount)

# Quick Sort

# Quick sort algroithm


# low=0 high=size-1 i=low j=i-1 pivot=arr[high]

# if(low<high):
#     while(i<=high-1):
#         if(arr[i]<=pivot):
#             j++
#             swap(arr[i],arr[j])
#             i++
#         else:
#             i++
#         swap(arr[j+1]<arr[high])
#     return j+1


# def quick(arr,low,high):
#     if(low<high):
#         part=partition(arr,low,high)
#         quick(arr,low,part-1)
#         quick(arr,part+1,high)
#     return arr
# def partition(arr,low,high):
#     i=low
#     j=i-1
#     pivot=arr[high]
#     while(i<=high-1):
#         if(arr[i]<=pivot):
#             j+=1
#             #swap(arr,arr[i],arr[j])
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#             i+=1
#         else:
#             i+=1
#     #swap(arr[j+1],pviot/arr[high])
#     temp=arr[j+1]
#     arr[j+1]=arr[high]
#     arr[high]=temp
#     return j+1

# size=int(input())
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(quick(arr,0,size-1))




#Linked LIst:
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    head=None
    def InsertAtBeg(self,data):
        newNode=node(data)
        if(self.head==None):
            self.head=newNode
            newNode.next=None
        else:
            newNode.next=self.head
            self.head=newNode

    def InsertAtEnd(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=None
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
                newNode.next=None
                temp.next=newNode
    
    def display(self):
        if(self.head==None):
            print("Empty !!")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
            print()
    
    def InsrtAtPos(self,pos,data):
        newNode=node(data)
        if(pos==1):
            self.InstertAtBeg(data)
        else:
            if(self.head==None):
                print("List is empty")
            else:
                temp=self.head
                



choice=1
ll=LinkedList()
while choice!=0:
    print("1. Insert at beg")
    print("2. Insert at end")
    print("3. Display")
    choice=int(input("Enter your choice : "))
    if(choice==1):
        data=int(input("Enter your choice : "))
        ll.InsertAtBeg(data)
    elif(choice==2):
        data=int(input("Enter your choice : "))
        ll.InsertAtEnd(data)
    elif(choice==3):
        ll.display()
    


#     def InsrtAtPos(self,pos,data):
#         newNode=node(data)
#         if(pos==1):
#             self.InstertAtBeg(data)
#         else:
#             if(self.head==None):
#                 print(list is )


# def InsertAtEnd(self,data):
#         newNode=node(data)
#         if self.head==None:
#             self.head=None
#         else:
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#                 newNode.next=None
#                 temp.next=newNode