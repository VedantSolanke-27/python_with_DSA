# Randam Question

# s = input("Enter a string: ")

# hashes = ""
# chars = ""

# for ch in s:
#     if ch == "#":
#         hashes += ch
#     else:
#         chars += ch

# result = hashes + chars

# print("Output:", result)

# Backtracking:

# arr=[1,2,3]
# def subset(index,result):
#     if index==len(arr):
#         print(result)
#         return
#     subset(index+1,result+ [arr[index]])

#     subset(index+1,result)

# subset(0,[])
#  call execution
# s[1,[1]] include
# s[2,[1,2]] include
# s[3,[1,2,3]] include
# S[1,[]] Exclude
# s[2,[1]] inclide
# s[3,[1,2]] include

# greedy algorithm:

# coins=[10,5,2,1]
# amount=25
# result=[]
# for i in coins:
#     while amount>=i:
#         result.append(i)
#         amount-=i
# print(result)
# print(len(result))

data = {}

def register():
    rollno = int(input("Enter roll no: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    if rollno not in data:
        data[rollno] = [name, age, marks]
        print("Student Registered Successfully!")
    else:
        print("Roll no already exists. Use another one!")

def Search():
    rollno = int(input("Enter roll no: "))

    if rollno not in data:
        print("Student is not in Database")
    else:
        print("Student is in database")

def Display():
    rollno = int(input("Enter roll no: "))

    if rollno in data:
        print(f"Name  -> {data[rollno][0]}")
        print(f"Age   -> {data[rollno][1]}")
        print(f"Marks -> {data[rollno][2]}")
    else:
        print("Student not Exist !!")

def Update():
    rollno = int(input("Enter roll no: "))

    if rollno in data:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        marks = int(input("Enter new marks: "))

        data[rollno] = [name, age, marks]
        print("Student data updated successfully!")
    else:
        print("Student not found!")

def Marks():
    rollno = int(input("Enter roll no: "))

    if rollno in data:
        marks = data[rollno][2]
        print(f"Marks of this student is {marks}")
    else:
        print("Student not found!")

choice = 1

while choice != 0:
    print("\n------ STUDENT MANAGEMENT SYSTEM ------")
    print("1. Register new Student")
    print("2. Display data of Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Enter/View Marks")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register()
    elif choice == 2:
        Display()
    elif choice == 3:
        Search()
    elif choice == 4:
        Update()
    elif choice == 5:
        Marks()
    elif choice == 0:
        print("Program Ended.")
    else:
        print("Invalid Choice!")