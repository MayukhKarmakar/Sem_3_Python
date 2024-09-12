
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}


length_student_dict = len(student)
print("Length of student dictionary:", length_student_dict)


skills_value = student['skills']
print("Value of skills:", skills_value)
print("Data type of skills:", type(skills_value))


student['skills'].extend(['HTML', 'CSS'])
print("Updated skills:", student['skills'])


keys_list = list(student.keys())
print("Dictionary keys as a list:", keys_list)


values_list = list(student.values())
print("Dictionary values as a list:", values_list)


items_list = list(student.items())
print("Dictionary as a list of tuples:", items_list)


del student['address']
print("Student dictionary after deleting 'address':", student)


del student
print("Student dictionary has been deleted.")
