student = {}

student['StdNo'] = input("Enter Student Number: ")
student['StuName'] = input("Enter Student Name: ")
student['StuAge'] = int(input("Enter Student Age: "))
student['StuCity'] = input("Enter Student City: ")

print("\nStudent Dictionary is:", student)
print("\nStudent Name is:", student['StuName'])
print("Student City is:", student['StuCity'])


print("\nAll Keys in Dictionary")
for key in student:
    print(key)


print("\nAll Values in Dictionary")
for key in student:
    print(student[key])


student['PhNo'] = input("Enter Phone Number: ")
print("\nUpdated Dictionary after adding Phone Number:", student)


student['StuName'] = input("Enter New Student Name: ")
print("\nUpdated Dictionary after changing name:", student)


student.pop('StuAge')
print("\nUpdated Dictionary after removing age:", student)


print("\nLength of Dictionary is:", len(student))


student_copy = student.copy()
print("\nCopied Dictionary is:", student_copy)


student.clear()
print("\nDictionary after clearing:", student)
