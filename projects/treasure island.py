print(''' 

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 

''') 


print ("Welcome to Treasure Island.\nYour mission is to find the treasure")

choice1 =input ("Type 'left' to go left or 'right' to go right: ")
 
if choice1 == "left" :
   choice2 = input ("type 'swim' or 'wait' : ")
   if choice2 == "wait" :
        choice3 = input("Which door? Red Or Blue or Yellow :")
        if choice3 == "yellow" :
            print("You Win!")
        elif choice3 == "red" :
            print("Burned by fire, Game Over.")
        elif choice3 == "blue" :
            print("Eaten by beasts, Game Over.")
        else :
            print("Game Over")
   else :
     print ("Game over")
else :
    print ("Game Over")



   