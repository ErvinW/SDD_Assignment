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
#score = 0
#coins = 16



    

class Building:
    def __init__(self):
        self.type = None
        self.row = None
        self.col = None

class Game:
    def __init__(self):
        self.coins = 1
        self.score = 0

def updateHighScores(playerName, score):
    file = open("ScoreFile.txt", "r")
    f = file.readlines()
    file.close()
    emptyFile = False

    if len(f) == 0:
        emptyFile = True

    newList = []
    for line in f:
        newList.append(line.strip())

    scoreList = []
    for x in range(1, len(newList), 2):
            scoreList.append(int(newList[x]))
        
    if len(newList) == 20:
        for index in range(0, len(scoreList), 1):
            if scoreList[index] < score:
                newList.pop(19)
                newList.pop(18)
                newList.insert(index * 2, playerName)
                newList.insert(index * 2 + 1, score)
                #scoreList.pop(9)
                #scoreList.insert(index, score)
                break
            elif scoreList[index] == score:
                if scoreList[9] == score:
                    return False
                else:
                    newList.pop(19)
                    newList.pop(18)
                    newList.insert(index * 2, playerName)
                    newList.insert(index *2 + 1, score)
                    #scoreList.pop(9)
                    #scoreList.insert(index, score)
                    break
    else:
        for index in range(0, len(scoreList), 1):
            if scoreList[index] <= score:
                newList.insert(index * 2, playerName)
                newList.insert(index * 2 + 1, score)
                break
            if index == len(scoreList):
                return False
    with open("ScoreFile.txt", "w") as file:
        if emptyFile == True:
            file.write(playerName + "\n" + str(score) + "\n")
        else:
            for value in newList:
                file.write(str(value) + "\n")
    file.close()
    return True

def init_turn(playerName, turn, score, coins):
    while True:
     if coins == 0 :
         print("\nGame over. Your score is " + str(score))
         boolValue = updateHighScores(playerName, score)
         if boolValue == True:
             print("\nCongratulations! Your score is in the top 10!")
         return
     
     turn += 1 

     buildingList = ['R', 'I', 'C', 'O', '*']
     random2building = random.sample(buildingList, 2)

     draw_map()
     print("Turn: {:<10} Score: {:<10}  Coins: {:<10}".format(str(turn), str(score), str(coins)))
     print("Options:")
     print("{:20}{:<20}{:>20}".format("1. Build", "2. Save and Exit", "3. Quit without saving"))
     action = input("Enter an action: ")
     if action == "1":
         print("Build")
         choice = input("Choose the building to build ({}/{}): ".format(random2building[0],random2building[1])).upper()
         while choice not in buildingList:
             print("Invalid building type.")
             choice = input("Choose the building to build ({}/{}): ".format(random2building[0],random2building[1])).upper()
             #turn -= 1
             
         
         else:
             coins -=1
             btype, row, col = build(turn, choice)
             score_to_add, coins_to_add = calculateScore(btype, row, col)
             score += score_to_add
             coins += coins_to_add
        
     elif action == "2":
         saveGame(playerName, turn, score, coins)
         return
     
     elif action == "3":
         print("Exited")
         return
     else:
         print("Next turn")
         init_turn(turn, score+3, coins-1)
     
     
def saveGame(playerName, turn, score, coins):
    
    saved_list = []
    saved_list.append(turn)
    saved_list.append(score)
    saved_list.append(coins)
    saved_list.append(playerName)
    
    datafile = open("SaveFile.txt", "w")
    for h in saved_list:
        datafile.write("{},".format(h))
    datafile.write("\n")
    
    for i in field:
        row = []
        for j in i:
            row.append(str(j))
        datafile.writelines("-".join(row))
        datafile.write("\n")
        
    datafile.close()
    print("Game Saved \n")
    
def loadGame():
    datafile = open("SaveFile.txt", "r")
    lines = datafile.readlines()
    playerSetting = lines[0].split(",")
    saved_field = lines[1:]
    
    #field = saved_field
    PlayerName = playerSetting[3]
    turn  = playerSetting[0]
    score = playerSetting[1]
    coins = playerSetting[2]
    
    for i in range(len(saved_field)):
        temp = saved_field[i].split("-")
        for j in range(len(temp)):
            if temp[j].strip("\n") == "[None, None]" or temp[j].strip("\n") == "[None, None, None]":
                field[i][j] = [None,None]
            else:
                unit = temp[j].strip("\n").strip("[").strip("]").split(",")
                field[i][j] = [unit[0].strip("'"),None, None]
    
def showHighScores():
    datafile = open("ScoreFile.txt", "r")
    lines = datafile.readlines()
    newList = []
    for line in lines:
        newList.append(line.strip())
    print("\n")
    for x in range (0, len(newList), 2):
        print(newList[x] + ", " + newList[x + 1])
    datafile.close()
     
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
        coins = 1
        turn = 0
        playerName = ""
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
                init_turn(playerName, turn, score, coins)
        elif option == '2':
                loadGame()
                init_turn(playerName, turn, score, coins)
                print("Map loaded from text file successfully!")
            

        elif option == '3':
             showHighScores()
    
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
     building.col = int(position[1:])
     building.row = ord(position[0].upper()) - ord('A')
     if turn == 1:
         field[building.row][building.col][0] = buildingType
         return buildingType, building.row, building.col
     else:
        index = letters.index(position[0].upper())
        check = validPosition(building.row, building.col)
        if check == True:
            field[building.row][building.col][0] = buildingType
            return buildingType, building.row, building.col
        else:
            while check != True:
                position = input("Enter the position: ")
                building.col = int(position[1:])
                building.row = ord(position[0].upper()) - ord('A')
                check = validPosition(building.row, building.col)
            field[building.row][building.col][0] = buildingType
            return buildingType, building.row, building.col
        
            
        

def calculateScore(btype, row, col):
    tempscore = 0
    tempcoins = 0
    indices_to_check = [
            (row, col-1), (row, col+1),
            (row-1, col), (row+1, col),
            (row-1, col-1), (row-1, col+1),
            (row+1, col-1), (row+1, col+1)
        ]
    if btype == "R":
        temp = ["R","C"]
        
        # Residential next to industry(I)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dr, dc in directions:
            try:
                if field[row + dr][col + dc][0] == "I":
                    tempscore += 1
            except:
                pass
        # Residential adjacent to Residential(R) or Commercial(C)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] in temp:
                    tempscore += 1
                if field[i][j][0] == "C":
                    tempcoins += 1
            except:
                pass
        # Residential(R) adjacent to Park(O)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] == "O":
                    tempscore += 2
            except:
                pass
    
    if btype == "I":
        tempscore += 1
        # Industry(I) adjacent to Residential(R)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] == "R":
                    tempcoins += 1
                    tempscore += 1
            except:
                pass
            
    if btype == "C":
        # Commercial(C) adjacent to Commercial(C)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] == "C":
                    tempscore += 1
            except:
                pass
        # Commercial (C) adjacent to Residential(R)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] == "R":
                    tempcoins += 1
                    tempscore += 1
            except:
                pass

    if btype == "O":
        # Park(O) adjacent to Park(O)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] == "O":
                    tempscore += 1
            except:
                pass
        # Park(O) adjacent to Residential(R)
        for i, j in indices_to_check:
            try:
                if field[i][j][0] == "R":
                    tempscore += 2
            except:
                pass
    
    if btype == "*":
        if field[row][col-1][0] == "*":
            tempscore += 1
        if field[row][col+1][0] == "*":
            tempscore += 1
            
    return tempscore, tempcoins

    
def validPosition(row, col):
    # A1
    if row == 0 and col == 0:
        if field[row+1][col][0] != None or field[row][col+1][0] != None: #or field[row+1][col+1][0] != None
            return True
        return False
    # A19
    if row == 0 and col == 19:
        if field[row][col-1][0] != None or field[row+1][col][0] != None: # or field[row-1][col+1][0] != None
            return True
        return False
    # T0
    if row == 19 and col == 0:
        if field[row][col+1][0] != None or field[row-1][col][0] != None: # or field[row-1][col+1][0] != None
            return True
        return False
    # T19
    if row == 19 and col == 19:
        if field[row][col-1][0] != None or field[row-1][col][0] != None: # or field[row-1][col-1][0] != None
            return True
        return False
    # Row A
    if row == 0:
        if field[row][col+1][0] != None or field[row][col-1][0] != None or field[row+1][col][0] != None: # or field[row+1][col-1][0] != None or field[row+1][col+1][0] != None
            return True
        return False
    # Row T
    if row == 19:
        if field[row][col+1][0] != None or field[row][col-1][0] != None or field[row-1][col][0] != None: # or field[row-1][col-1][0] != None or field[row-1][col+1][0] != None
            return True
        return False
    # Column 0
    if col == 0:
        if field[row+1][col][0] != None or field[row-1][col][0] != None or field[row][col+1][0] != None: # or field[row+1][col+1][0] != None or field[row-1][col-1][0] != None
            return True
        return False
    # Column 19
    if col == 0:
        if field[row+1][col][0] != None or field[row-1][col][0] != None or field[row][col-1][0]: # != None or field[row-1][col-1][0] != None or field[row+1][col+1][0] != None
            return True
        return False
    # The rest 
    if field[row][col-1][0] != None or field[row][col+1][0] != None or field[row-1][col][0] != None or field[row+1][col][0] != None:
        return True
    return False


show_main_menu()