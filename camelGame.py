

print("Welcome to Camel!")
print("You have stolen a Nomadic camel to make your way across the Great Gobi Desert.\nThe camel's owners want their camel back and are chasing you down! \nSurvive your desert trek and outrun the Nomads.")
 # Gobi desert is 1000 miles long


sandwich = False

Drink_From_Your_Canteen = 1
Slow_Trot = 2
Full_Speed_Ahead = 3
Take_A_Rest = 4
Quit = 5
choice = 1

while False == sandwich:
    print("What Do You Preffer To Do")
    print("Drink From Your Canteen = 1\nSlow Trot = 2\nFull Speed Ahead = 3\nTake A Rest = 4\nQuit = 5 ")
    key = str(input("make a choice"))
    if key == "1" :
        choice = Drink_From_Your_Canteen
    if key == "2" :
         choice = Slow_Trot
    if key == "3":
        choice = Full_Speed_Ahead
    if key == "4":
        choice = Take_A_Rest
    if key == "5":
        choice = Quit


if choice == Quit:
    print ("You Quit!\n The Nomads Find Your hideout being circled with vultures.\n your was found body with an empty canteen and the camel tied to a rock nearby. \nYou have lost and Failed to escape the Great Gobi Desert. ")
    print("GAME OVER! \n  _\nC') , ,\n ( \/^U^\ \n  (      \ \n   i(__.i\*\n   /|   / \ \n o u  o   o")
    sandwich = True