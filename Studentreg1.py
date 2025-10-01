#Student registration system

# NEEDS
#datastruktur för studenter 
# loop för menyn
# Menyn har 3 val: add studen 2. list student. 4. quit.

student_list =[]

print("Welcome to the studentregister!")

while True:
    print("--MENU--")
    print("1. Add student")
    print("2. List Students")
    print("3. Search student")
    print("4. Quit program")


    menu_choice = input("choose 1-4: ")

    if menu_choice == "1":
        new_student_name = input("New student name:")
        new_student_age = input ("New student Age")
        new_student_dict = {"name": new_student_name, "Age": new_student_age}
        student_list.append(new_student_dict)
        print("New student created:")
        print(f"name: {new_student_dict["name"]}), Age: {new_student_dict["Age"]}")
        #print(f"age:" {new_student_dict["age"]}")
    elif menu_choice == "2":
        for student in student_list:
            print(f"name: {student["name"]}, Age: {student["Age"]}")

    elif menu_choice == "3":
        student_searched = input("search student: ")
        found = False
        for student in student_list:
            if student["name"] == student_searched:
                found = True
                print(f"student found: {student}")
                break
        if not found:
            print("student not found")
        
    
    elif menu_choice == "4":
        print("student: ")
        print(student_list)
        quit()
    else: 
        print("choice not valid. Please choose a menu 1-4.")
    sum_age = 0
    for student in student_list:
        sum_age += int(student["Age"])
#beräkna genomsnitts ålder på studenterna

    if student_list:
        average_age = sum_age / len(student_list)
        print(f"Genomsnittlig ålder: {average_age}")
    else:
        print("Inga studenter registrerade.")
