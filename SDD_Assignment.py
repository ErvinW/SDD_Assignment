##SDD Assignment 
## Done by Ervin, Xin Yin, Xue Wen, Keene, Bi De
import random
from User import User

class Building:
    def __init__(self, type):
        self.name = type
        self.row = None
        self.col = None


field = [[[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]]
    ]

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

playerName = ""







def init_turn(turn, score, coins):
    while True:
     turn += 1 

     buildingList = ['R', 'I', 'C', 'O', '*']
     random2building = random.sample(buildingList, 2)

     draw_map()
     print("Turn: {} {:>10}{:>10}".format(str(turn), str(score), str(coins)))
     print("Options:")
     print("{:20}{:<20}{:>20}".format("1. Build", "2. Save and Exit", "3. Quit without saving"))
     action = input("Enter an action: ")
     if action == "1":
         print("Build")
         print("Choose the building to build ({}/{})".format(random2building[0],random2building[1]))
        
     elif action == "2":
         print("game saved")
         return
     
     elif action == "3":
         print("Exited")
         break
     else:
         print("Next turn")
         init_turn(turn, score+3, coins-1)
     
     

     
def draw_map():
    borders = "+-----"
    end = "+"
    rows = len(field)
    columns = len(field[0])
    for i in range(0, 19):
        print("{:>6}".format(i), end="")
    print("{:>6}".format("19"))
    print()
    
    
    
    print("  ",end="")
    for i in range(columns):
        print(borders,end="")
    print(end)
    
    
   


    for i in range(rows):
        print(letters[i],end="")
        print(" ",end="")
        for j in field[i]:
            print("|",end="")
            if j[0] == None:
                print("{:^5}".format(""),end="")
            else:
                print("{:^5}".format(str(j[0])),end="")
        print("|")
        print("  ",end="")

        for j in field[i]:
            print("|",end="")
            if j[1] == None:
                print("{:^5}".format(""),end="")
            else:
                print("{:2}/{:2}".format(j[1],j[2]),end="")
        print("|")

        print("  ",end="")  #To leave a space in the column that has a letter
        for i in range(columns):
            print(borders,end="")
        print(end)

def show_main_menu():
    while True:
        score = 0 
        coins = 16
        turn = 0
        print()
        print("----------------")
        print("| Ngee Ann City |")
        print("----------------")
        print("Build the most prosperous city!")
        print()

        print("Please select an option \n\
        1. Start New Game\n\
        2. Load Saved Game\n\
        3. Display High Scores\n\
        4. Exit")
        option = input("Enter your choice: ")
        if option == '1':
                init_turn(turn, score, coins)
                
            

        elif option == '2':
                ## Add in code to read save file     
                print("Map loaded from text file successfully!")
            

        elif option == '3':
             print("High score in progress")
    
        elif option == '4':
                print("Goodbye")
                return False
            
    
        else:
            print("Invalid option. Please enter a valid choice.")
            return

        
def build(turn, type):
     building = Building()
     if turn == 1:

         position = input("Enter the position: ")
         building.row = ''.join(filter(str.isalpha, position))
         building.col = ''.join(filter(str.isdigit, position))

            



show_main_menu()