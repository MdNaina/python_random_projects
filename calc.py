import time
while True:
	time.sleep(3)
	print("_________________________________")
	print("| Option                        |".title())
	print("| type 'add' to addition        |")
	print("| type 'sub' to subraction      |")
	print("| type 'mul' to multiplication  |")
	print("| type 'div' to division        |")
	print("| type 'quit' to exit the calc  |")
	print("_________________________________")
	cmd = input("> ")

	if cmd == "quit":
		break
	elif cmd == "add":
		num1 = float(input("enter the first number  :"))
		num2 = float(input("enter the second number :"))
		result = str(num1 + num2)
		print("="+ result)

	elif cmd == "sub":
		num1 = float(input("Enter the first number : "))
		num2 = float(input("Enter the second number: "))
		result = str(num1 - num2)
		print("="+result)

	elif cmd == "mul":
		num1 = float(input("Enter the first number : "))
		num2 = float(input("Enter the second number: "))
		result = str(num1 * num2)
		print("="+result)

	elif cmd == "div":
		num1 = float(input("Enter the first number : "))
		num2 = float(input("Enter the second number: "))
		result = str(num1 / num2)
		print("="+result)
	else:
		print("Unknown Command")
