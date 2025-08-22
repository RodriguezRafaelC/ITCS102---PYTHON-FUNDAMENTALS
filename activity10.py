name = input("Enter your name : ")
balance = 1000
print("Hello", name, "Your remaining balance is", int(balance) , "how much would you like to pay")
payment = eval(input("$ : "))

if payment <= 1000:
	balance = balance - payment
	print(name, "paid", payment)
	print("payment successful your remaining balance is", balance)
else:
	payment = payment - balance
	print("Thank you, here is your change", payment)