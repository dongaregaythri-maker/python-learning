# 1. Reverse a number
num = 12345
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)



# Output: 54321

# 2. Check whether a number is palindrome
num = 121
temp = num
rev = 0
while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        if temp == rev:
           print("Palindrome")
        else:
           print("Not Palindrome")



# Output: Palindrome

# 3. Check whether a number is prime
num = 17
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")



# Output: Prime

# 4. Find factorial of a number
num = 5
fact = 1
for i in range(1, num + 1):
        fact *= i
print(fact)



# Output: 120

# 5. Find Fibonacci series
n = 7
a = 0
b = 1
for i in range(n):
        print(a, end=" ")
        a, b = b, a + b



# Output: 0 1 1 2 3 5 8

# Level 2: String coding questions
# 6. Reverse a string without using slicing
text = "python"
rev = ""
for ch in text:
        rev = ch + rev
print(rev)



# Output: nohtyp

# 7. Count vowels in a string
text = "programming"
count = 0
for ch in text:
        if ch in "aeiou":
                    count += 1
                    print(count)



# Output: 3

# 8. Check whether a string is palindrome
text = "madam"
if text == text[::-1]:
        print("Palindrome")
else:
       print("Not Palindrome")



# Output: Palindrome

# 9. Count frequency of each character
text = "banana"
freq = {}
for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
        print(freq)



# Output:
# {'b': 1, 'a': 3, 'n': 2}



# Level 3: List coding questions
# 10. Find the second-largest number
numbers = [10, 25, 5, 40, 30]
unique = list(set(numbers))
unique.sort()
print(unique[-2])



# Output: 30

# 11. Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
result = []
for num in numbers:
        if num not in result:
                    result.append(num)
print(result)



# Output: [1, 2, 3, 4, 5]

# 12. Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = []
for num in a:
        if num in b:
           common.append(num)
           print(common)



# Output: [3, 4]
# Level 4: Tricky interview coding

# 13. Find missing number in a sequence
numbers = [1, 2, 3, 5, 6]
n = 6
total = n * (n + 1) // 2
missing = total - sum(numbers)
print(missing)



# Output: 4

# 14. Find pairs whose sum equals a target
numbers = [2, 4, 3, 5, 7, 8]
target = 7
for i in range(len(numbers)):
       for j in range(i + 1, len(numbers)):
              if numbers[i] + numbers[j] == target:
                      print(numbers[i], numbers[j])



# Outpu/t:
# 2 5
# 4 3


# 15. Find the largest word in a sentence
sentence = "Python is an interesting programming language"
words = sentence.split()
largest = ""
for word in words:
    if len(word) > len(largest):
            largest = word
print(largest)



# Output: programming

# Your coding practice challenge
# Try these five without looking at the solutions first.

# Question 1

# Write a program to find the sum of digits of a number.

# Question 2

# Write a program to find the largest and smallest elements in a list.

# Question 3

# Write a program to check whether two strings are anagrams.

# Question 4

# Write a program to print this pattern:
# 1
# 12
# 123
# 1234
# Show hint

# [ ] 
# Question 5

# Write a function to find the sum of all even numbers in a list.
