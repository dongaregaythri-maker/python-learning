a = int(input("Enter your age: "))
if(a<=18):
    print("You are a minor.")
    print("You are not eligible to vote.")
elif(a<0):
   print("You are entering invalid negative age.")
elif(a>120):
    print("You are entering invalid age greater than 120.")
else:
    print("You are an adult.")
    print("You are eligible to vote.")