print("You have eaten in a carinderya near school")
name = input("Enter your name : ")
bill = input("Enter your payment please : ")
student = input("Are you a student? (yes/no) : ").lower()

if student == "yes":
    discount = bill * 0.2
    newBill = bill - discount
    print("Students has a discount of 20%\nYour total payment is",newBill)
else:
    print("You have no discount.")