import os

print("STUDENT INFORMATION SYSTEM")
print("-------------------------------------------------\n")

student_records = {}

while True:
    print("Select from the options below \nA- Add informations\nB - Search for records \nC - Delete a record \nD - Modify a record \nE - Exit")

    choice = input("Enter Your choice : ").upper()

    if choice == "A":
        identification_num = input("Enter Student Identification Number : ")
        first_name = input("Enter Fist Name : ").upper()
        last_name = input("Enter Last Name : ").upper()
        course = input("Enter Course : ").upper()
        email = input("Enter Email : ")
        isSingle = input("Are you single(True or False) : ")
        print("Record has been saved")
        student_records = {identification_num : [first_name, last_name, email, isSingle]}
        
        os.system('cls')
        continue

    elif choice == "B":
        student_id = input("Enter Student Identification Number : ")
        for j in student_records.keys():
            if student_id in student_records.keys():
                print("Record Found!")

                for i in student_records[student_id]:
                    print(" -", i)

            else:
                print("No Record found!")

        continue

    elif choice == "C":
        delete = input("What ID will you delete : ")
        for j in student_records.keys():
            if delete in student_records.keys():
                del student_records.keys()


