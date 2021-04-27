from termcolor import colored, cprint

"""
0 - 12
 | | | | | |   0
-------------  1 
 | | | | | |   2
-------------  3
 | | | | | |   4
-------------  5
 | | | | | |   6
-------------  7
 | | | | | |   8
-------------  9
 | | | | | |  10
"""
def drawConnectFour(field):
    for row in range(11):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            for col in range(13):
                if col % 2 == 0:
                    practicalCol = int(col / 2)
                    if col != 12:
                        cprint(field[practicalCol][practicalRow],end="")
                    else:
                        cprint(field[practicalCol][practicalRow])
                else:
                    cprint("|",end="")
        else:
            cprint("-------------")

currentField = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    
drawConnectFour(currentField)

def playConnectFour():
    
    Player = 1
    
    while(True):
        
        try:
            column = input(f"Player {Player} please enter the column for your piece: ")
            if column.isnumeric() == False:
                raise TypeError
        except:
            print("Type Error! You must input a number between 1 - 7")
            column = input(f"Player {Player} please enter the column for your piece again: ")
            while column.isnumeric() == False:
                print("Type Error! You must input a number between 1 - 7")
                column = input(f"Player {Player} please enter the column for your piece again: ")

        if Player == 1:
            n = 5
            while n > -1 :
                if currentField[int(column)-1][n] != " ":
                    n -= 1
                    continue
                else:
                    currentField[int(column)-1][n] = colored(u'\u2B24',"red")
                    break
            Player = 2        
        else:
            n = 5
            while n > -1 :
                if currentField[int(column)-1][n] != " ":
                    n -= 1
                    continue
                else:
                    currentField[int(column)-1][n] = colored(u'\u2B24',"blue")
                    break
            Player = 1   
                
        drawConnectFour(currentField)


playConnectFour()


    

