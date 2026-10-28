# 1. What is a nested dictionary?

# A nested dictionary is a dictionary inside another dictionary.

# In simple words, one dictionary contains another dictionary as its value.

# Example :

student = {
    "student1":{
        "name": "Rahul"
        "age" : 20
    }
    "student2": {
        "name": "priya"
        "age" : 23
    }
}
print(students)

# Here:
# - students is the outer dictionary.
# - "student1" and "student2" are keys of the outer dictionary.
# - Each student's information is stored in an inner dictionary.

# 2. How to access values in a nested dictionary
# Use two sets of square brackets: the first accesses the outer dictionary, and the second accesses the inner dictionary.

students = {
    "student1": {"name": "Rahul", "age": 21},
    "student2": {"name": "Priya", "age": 22}
}

print(students["student1"]["name"])
print(students["student2"]["age"])

# Explanation:
# - students["student1"] selects Rahul's dictionary.
# - ["name"] accesses Rahul's name.
# - students["student2"]["age"] accesses Priya's age.

# 3. How to update a value

students = {
    "student1": {"name": "Rahul", "age": 21}
}

students["student1"]["age"] = 22

print(students["student1"])

# 4. How to add a new key-value pair

students = {
    "student1": {"name": "Rahul", "age": 21}
}

students["student1"]["city"] = "Pune"

print(students)

# 5. How to loop through a nested dictionary

students = {
    "student1": {"name": "Rahul", "age": 21},
    "student2": {"name": "Priya", "age": 22}
}

for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(key, ":", value)

# 7. Interview practice question

# Question: Write a program to print the name of the second employee.

employees = {    "emp1": {"name": "Ravi", "salary": 25000}, 
                "emp2": {"name": "Neha", "salary": 30000}}# Write your code here


# Hint: Access the outer key "emp2" first, then the inner key "name".

# The expected output is:
# Neha


# Remember: outer_dictionary[outer_key][inner_key] is the basic pattern for accessing a value in a nested dictionary.