print("welcome to xyz pizza order your pizza")
size = input("which size of pizza do you Want(S, M, L) : ")
pep = input("do you want pepperoni on your pizza(Y,N):")
ex_chiz = input ("do you want extra chiz(y, n):")
bill = 0

if size=="s" :
    bill += 1
   
elif size == "m" :
    bill += 2
    
elif size == "l" :
    bill += 3
    
else :
    print ("order something")


if pep == "y" :
    bill += 1
else :
    bill

if ex_chiz == "y" :
    bill += 1
else :
    bill


print(f"your bill is {bill}")






    
    

    



   