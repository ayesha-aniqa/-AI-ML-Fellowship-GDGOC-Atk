#!/usr/bin/env python
# coding: utf-8

# In[2]:


students = []

#adding student record
def add_student(name, reg, course):
    student = {
        'name': name,
        'reg': reg,
        'course': course
    }
    students.append(student)
    print("Student added successfully.")

#updating student record
def update_student(reg):
    for s in students:
        if s['reg'] == reg:
            new_name = input("Enter new name: ")
            new_course = input("Enter new course: ")

            if new_name:
                s['name'] = new_name
            if new_course:
                s['course'] = new_course

            print("Update successful.")
            return

    print("Record not found.")

#display student record
def display():
    if not students:
        print("No record found.")
        return

    for s in students:
        print(s)


        #functions calling
while True:
    choice = input(
        "\n1. Add student information\n 2. Update student information\n 3. Display student information\n 4. Exit\n Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        reg = input("Enter registration number: ")
        course = input("Enter course: ")
        add_student(name, reg, course)

    elif choice == '2':
        reg = input("Enter registration number to update: ")
        update_student(reg)

    elif choice == '3':
        display()

    elif choice == '4':
        print("Exiting.")
        break

    else:
        print("Invalid choice.")


# In[ ]:




