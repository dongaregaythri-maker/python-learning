a = int(input("Enter your age: "))
#this is first if ststement
if(a%2 == 0):
    print("a is even")
else:
    print("a is odd")
#the first if ends here 
#second if starts here
if(a<=18):
    print("You are a minor.")
    print("You are not eligible to vote.")

else:
    print("You are an adult.")
    print("You are eligible to vote.")
#the second if ends here