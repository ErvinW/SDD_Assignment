# SDD Assignment 
# Done by Ervin, Xin Yin, Xue Wen, Keene, Bi De
import random
from User import User


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


class Building:
    def __init__(self):
        self.type = None
        self.row = None
        self.col = None




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
         choice = input("Choose the building to build ({}/{})".format(random2building[0],random2building[1])).upper()
         if choice not in buildingList:
             print("Invalid building type.")
             turn -= 1
             return
         else:
             coins -=1
             build(turn, choice)
        
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
                playerName = input("Username: ")    
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

        
def build(turn, buildingType):
     building = Building()
     building.type = buildingType
     position = input("Enter the position: ")
     building.col = int(position[1])
     building.row = ord(position[0].upper()) - ord('A')
     if turn == 1:
         field[building.row][building.col][0] = buildingType
     else:
        index = letters.index(position[0].upper())
        check = validPosition(building.row, building.col)
        if check == True:
            field[building.row][building.col][0] = buildingType
        else:
            while check != True:
                position = input("Enter the position: ")
                building.col = int(position[1])
                building.row = ord(position[0].upper()) - ord('A')
                check = validPosition(building.row, building.col)
            field[building.row][building.col][0] = buildingType
        

        

    
def validPosition(row, col):
    # A1
    if row == 0 and col == 0:
        if field[row+1][col][0] != None or field[row][col+1][0] != None or field[row+1][col+1][0] != None:
            return True
        return False
    # A19
    if row == 0 and col == 19:
        if field[row][col-1][0] != None or field[row+1][col][0] != None or field[row-1][col+1][0] != None:
            return True
        return False
    # T0
    if row == 19 and col == 0:
        if field[row][col+1][0] != None or field[row-1][col][0] != None or field[row-1][col+1][0] != None:
            return True
        return False
    # T19
    if row == 19 and col == 19:
        if field[row][col-1][0] != None or field[row-1][col][0] != None or field[row-1][col-1][0] != None:
            return True
        return False
    # Row A
    if row == 0:
        if field[row][col+1][0] != None or field[row][col-1][0] != None or field[row+1][col][0] != None or field[row+1][col-1][0] != None or field[row+1][col+1][0] != None:
            return True
        return False
    # Row T
    if row == 19:
        if field[row][col+1][0] != None or field[row][col-1][0] != None or field[row-1][col][0] != None or field[row-1][col-1][0] != None or field[row-1][col+1][0] != None:
            return True
        return False
    # Column 0
    if col == 0:
        if field[row+1][col][0] != None or field[row-1][col][0] != None or field[row][col+1][0] != None or field[row-1][col-1][0] != None or field[row+1][col+1][0] != None:
            return True
        return False
    # Column 19
    if col == 0:
        if field[row+1][col][0] != None or field[row-1][col][0] != None or field[row][col-1][0] != None or field[row-1][col-1][0] != None or field[row+1][col+1][0] != None:
            return True
        return False
    # The rest 
    for i in range(row-1,row+2):
        for x in range(col-1,col+2):
            if field[i][x][0] != None:
                return True
    return False


# (1,2)  (1,3)  (1,4)           
# (2,2)  (2,3)  (2,4)  
# (3,2)  (3,3)  (3,4)


show_main_menu()