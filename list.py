# write the code..
numbers = []

while True:
	print("1. Add\n2. Remove\n3. Display\n4. Quit")
	choice = int(input("Enter choice: "))

	if choice == 4:
		break

	elif choice == 1:
		add = int(input("Integer: "))
		numbers.append(add)
		print("List after adding:", numbers)
	

	elif choice == 2:
		if not numbers:
			print("List is empty")
		else:
			remove = int(input("Integer: "))
			if remove not in numbers:
				print("Element not found")
			else:
				numbers.remove(remove)
				print("List after removing:", numbers)

	elif choice == 3:
		if not numbers:
			print("List is empty")
		else:
			print(numbers)

	else:
		print("Invalid choice")