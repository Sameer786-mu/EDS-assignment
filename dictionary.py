# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...
print("Original Dictionary:", student)

key = int(input())
value = input()
student[key] = value
print("After Insertion:", student)

key = int(input())
value = input()
if key in student:
	student[key] = value
print("After Update:", student)

key = int(input())
if key in student:
	del student[key]
print("After Deletion:", student)


print("Traversing Dictionary:")
for k, v in student.items():
	print(k, ":", v)

