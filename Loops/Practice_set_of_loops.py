#write the program to print multiplication table of given number using for loop 
n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n * i}")

#write a program to greet all the person names stored in a list and which start with g

l=["Gaythri", "John", "Alice", "Bob", "Eve","Gayu","Guddy"]

for name in l:
    if (name.startswith("G")):
        print(f"hello {name}")

#write the program to print multiplication table of given number using while loop

n = int(input("Enter the number: "))
i=1
while i<11:
    print(f"{n} * {i} = {n * i}")

