import os
import json

os.system('cls')


print(" -STUDENT INFORMATION SYSTEM-")

student_records = {}

while True:
    print("\n==========================================\n")
    print('''
                  -Select from the options below-
          A - Add informations
          B - Search for records
          C - Delete a record
          D - Modify a record
          E - Export Data
          F - Import Data
          P - Print All Data
          X - Exit
          ''')
    print("==========================================\n")

    choice = input("Enter Your choice : ").upper() #Enter the program you want to do

    if choice == "A":
        print("\n-Add a new Student Record-") 
        print("==========================================\n")
        identification_num = input("Enter Student Identification Number : ") #add a value for the dictionary list

        if identification_num in student_records.keys(): #record checker to see if the id already exist
            print("\nRecord already existed!\n")
            continue
        
        first_name = input("Enter Fist Name : ").upper()
        last_name = input("Enter Last Name : ").upper()
        course = input("Enter Course : ").upper()
        email = input("Enter Email : ")
        isSingle = input("Are you single(True or False) : ")
        student_records[identification_num] = [first_name, last_name, email, isSingle] #create multiple records
        print("Record has been saved")
        
    elif choice == "B":
        os.system('cls')

        print("\nSearch for Student Record")
        print("==========================================\n")
        student_id = input("Enter Student Identification Number : ") #search the id
        for j in student_records.keys():
            if student_id in student_records.keys(): #check if id exist in the dict
                print("==========================================\n")
                print("Record Found\n")
                print(f"{student_id} Record")
                print("==========================================\n")

                for i in student_records[student_id]: #iterate the dict or list
                    print(" -", i) #print the value inside the dict
                break

            else:
                print("==========================================\n")
                print("No Record found!\n")
        
        continue

    elif choice == "C":

        os.system("cls")

        delete = input("What ID will you delete : ").lower()
        if delete not in student_records.keys():
            print("No Record found!")
        else:
            delete_check = input(f"Are you sure you want to delete {delete}? (yes/no) : ").lower()
            if delete_check == "no":
                continue
            elif delete_check == "yes":
                student_records.pop(delete)
                print(f"{delete} has successfully deleted")
                continue
            else:
                print("Invalid input")

    elif choice == "D":
        os.system('cls')
        student_id = input("Enter Student Identification Number : ") #search the id
        for j in student_records.keys():
            if student_id in student_records.keys(): #check if id exist in the dict
                print("==========================================\n")
                print("Record Found\n")
                print(f"Student ID number {student_id} Record")
                print("==========================================\n")

                for i in student_records[student_id]: #iterate the dict or list
                    print(" -", i) #print the value inside the dict

                first_name = input("Enter New Fist Name : ").upper()
                last_name = input("Enter New Last Name : ").upper()
                course = input("Enter New Course : ").upper()
                email = input("Enter New Email : ")

                student_records[student_id][0] = first_name
                student_records[student_id][1] = last_name
                student_records[student_id][2] = course
                student_records[student_id][3] = email

                print("Record Has Successfully Updated!")
                
            else:
                print("Record not found")

    elif choice == "E":
        os.system('cls')
        print("Export Student Record")
        with open("student_record.json", "w") as new_file:
            json.dump(student_records, new_file, indent=4)

        print("Data has been saved")

    elif choice == "F":
        os.system('cls')
        print("Import Student Record")

        with open("student_record.json", "r") as new_file:
            student_json = json.load(new_file)

        student_records = student_json
        print("Data imported to json")

    elif choice == "P":
        os.system('cls')
        for i in student_records[student_id]: #iterate the dict or list
                    print(" -", i) #print the value inside the dict