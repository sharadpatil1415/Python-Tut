num0 = input("enter the number : ") 
num = int(num0)
if (num < 0) :
    print("number is negative")
elif(num > 0):
    if(num <= 10):
        print("nember is between 1-10")
    elif(num >= 10 and num <= 20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")    
      
else:
    print("number is zero")    