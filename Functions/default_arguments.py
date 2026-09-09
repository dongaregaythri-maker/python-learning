#the default argument work like if you give the value then it will take that value otherwise it will take the default value
#value is given 
def good_day(name, ending="welcome"):
    print("good day " + name)
    print(ending)  

good_day("gayithri", "thankyou")

#value is not given so it will take the default value
def good_day(name, ending="welcome"):
    print("good day " + name)
    print(ending)  

good_day("gayithri", )