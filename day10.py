file = open("D:\Python\CodeAdvent2023\day10_input.txt","r")
class Pipe():
    def __init__(self,input):
        self.icon = input
        self.north = "|LJ".count(input)>0
        self.south = "|7F".count(input)>0
        self.east = "-LF".count(input)>0
        self.west = "-J7".count(input)>0
        self.is_pipe="S|-LJ7F".count(input)>0
        self.is_loop = False
        self.interior = False
        self.exterior = False
        self.distance = 99999
    def __str__(self):
        #return f"{self.icon}"
        #if not self.is_pipe: return "."
        #if self.distance > 20000: return self.icon
        #return f"{self.distance}"
        if self.interior: return "I"
        if self.is_loop: return self.icon
        if self.exterior: return "O"
        
        return "#"
def parseList(input):
    list = []
    for i in input:
        temp = []
        for j in i.rstrip():
            temp.append(Pipe(j))
        list.append(temp)
    return list
def printMaze():
    for i in list:
        string = ""
        for j in i: 
            string = string + str(j)
        print(string)
def findIcon(input,partTwo):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if  list[i][j].icon == input:
                if partTwo and list[i][j].is_loop and list[i-1][j].exterior:return [i,j]
                if not partTwo: return [i,j]
def checkEast(x,y):
    if y < len(list[x])-1: return list[x][y+1].west and list[x][y].east
    return False
def checkWest(x,y):
    if y > 0: return list[x][y-1].east and list[x][y].west
    return False
def checkNorth(x,y):
    if x > 0: return list[x-1][y].south and list[x][y].north
    return False
def checkSouth(x,y):
    if x < len(list)-1: return list[x+1][y].north and list[x][y].south
    return False
def loopFromPos(x,y,partTwo):
    if not partTwo:
        list[x][y].is_loop = True
        if list[x-1][y].south: list[x][y].north = True
        if list[x+1][y].north: list[x][y].south = True
        if list[x][y+1].west: list[x][y].east = True
        if list[x][y-1].east: list[x][y].west = True
    if checkNorth(x,y):
        blocked = "south"
        current_x = x - 1
        current_y = y
        if partTwo:doTheLoopTwo(current_x,current_y,x,y,blocked)
        else:doTheLoop(current_x,current_y,x,y,blocked)
    if checkSouth(x,y):
        blocked = "north"
        current_x = x + 1
        current_y = y
        if partTwo:doTheLoopTwo(current_x,current_y,x,y,blocked)
        else:doTheLoop(current_x,current_y,x,y,blocked)
    if checkEast(x,y):
        blocked = "west"
        current_x = x 
        current_y = y + 1
        if partTwo:doTheLoopTwo(current_x,current_y,x,y,blocked)
        else:doTheLoop(current_x,current_y,x,y,blocked)
    if checkWest(x,y):
        blocked = "east"
        current_x = x 
        current_y = y - 1
        if partTwo:doTheLoopTwo(current_x,current_y,x,y,blocked)
        else:doTheLoop(current_x,current_y,x,y,blocked)
def doTheLoop(current_x,current_y,x,y,blocked):
    current_dist = 1
    while current_x - x or current_y -y:
        list[current_x][current_y].distance = min(list[current_x][current_y].distance,current_dist)
        list[current_x][current_y].is_loop=True
        #print(current_x,current_y, current_dist, blocked,)
        if not blocked == "north" and checkNorth(current_x,current_y):
            blocked = "south"
            current_x+=-1
            #print("Went N")
        elif not blocked == "south" and checkSouth(current_x,current_y):
            blocked = "north"
            current_x+=1
            #print("Went S")
        elif not blocked == "east" and checkEast(current_x,current_y):
            blocked = "west"
            current_y+=1
            #print("Went E")
        elif not blocked == "west" and checkWest(current_x,current_y):
            blocked = "east"
            current_y+=-1
            #print("Went W")
        else: print("bad")
        current_dist+=1
def doTheLoopTwo(current_x,current_y,x,y,blocked):
    starting = list[current_x][current_y].icon
    ext_nw, ext_ne, ext_sw, ext_se = True, True, False, False
    if starting == "F":
        ext_sw = True
    elif starting == "7":
        ext_se = True
    while current_x - x or current_y -y:
        #print(current_x,current_y, current_dist, blocked)
        if not blocked == "north" and checkNorth(current_x,current_y):
            blocked = "south"
            current_x+=-1
            ext_sw = ext_nw
            ext_se = ext_ne
            if list[current_x][current_y].north: ext_ne, ext_nw = ext_se, ext_sw
            #elif list[current_x][current_y].south:ext_ne, ext_se = ext_nw, ext_nw
            elif list[current_x][current_y].east: ext_nw, ext_ne = ext_sw, ext_sw
            elif list[current_x][current_y].west: ext_nw, ext_ne = ext_se, ext_se
            #print("Went N")
        elif not blocked == "south" and checkSouth(current_x,current_y):
            blocked = "north"
            current_x+=1
            ext_nw = ext_sw
            ext_ne = ext_se
            #if list[current_x][current_y].north: ext_ne, ext_se = ext_sw, ext_sw
            if list[current_x][current_y].south:ext_se, ext_sw = ext_ne, ext_nw
            elif list[current_x][current_y].east: ext_se, ext_sw = ext_nw, ext_nw
            elif list[current_x][current_y].west: ext_se, ext_sw = ext_ne, ext_se
            #print("Went S")
        elif not blocked == "east" and checkEast(current_x,current_y):
            blocked = "west"
            current_y+=1
            ext_nw = ext_ne
            ext_sw = ext_se
            if list[current_x][current_y].north: ext_ne, ext_se = ext_sw, ext_sw
            elif list[current_x][current_y].south:ext_ne, ext_se = ext_nw, ext_nw
            elif list[current_x][current_y].east: ext_ne, ext_se = ext_nw, ext_sw
            #elif list[current_x][current_y[.west: ext_nw, ext_sw = ext_ne, ext_se
            #print("Went E")
        elif not blocked == "west" and checkWest(current_x,current_y):
            blocked = "east"
            current_y+=-1
            ext_ne =ext_nw 
            ext_se = ext_sw
            if list[current_x][current_y].north: ext_nw, ext_sw = ext_se, ext_se
            elif list[current_x][current_y].south:ext_nw, ext_sw = ext_ne, ext_ne
            #elif list[current_x][current_y].east: ext_ne, ext_se = ext_nw, ext_sw
            elif list[current_x][current_y].west: ext_nw, ext_sw = ext_ne, ext_se
            #print("Went W")
        else: print("bad")
        
        #check nearby neighbors for interiors
        if current_x > 0 and current_x < len(list)-1 and current_y > 0 and current_y < len(list[0])-1:
            if ext_nw and ext_ne and not list[current_x-1][current_y].is_loop: list[current_x-1][current_y].exterior = True
            if ext_ne and ext_se and not list[current_x][current_y+1].is_loop: list[current_x][current_y+1].exterior = True
            if ext_sw and ext_se and not list[current_x+1][current_y].is_loop: list[current_x+1][current_y].exterior = True
            if ext_sw and ext_nw and not list[current_x][current_y-1].is_loop: list[current_x][current_y-1].exterior = True
            if not ext_nw and not ext_ne and not list[current_x-1][current_y].is_loop: list[current_x-1][current_y].interior  = True
            if not ext_ne and not ext_se and not list[current_x][current_y+1].is_loop: list[current_x][current_y+1].interior  = True
            if not ext_sw and not ext_se and not list[current_x+1][current_y].is_loop: list[current_x+1][current_y].interior  = True
            if not ext_sw and not ext_nw and not list[current_x][current_y-1].is_loop: list[current_x][current_y-1].interior = True
def floodFillExterior():
    # loop 1: get all edges marked as exterior.
    # walk right and left marking all nearby to exterior as exterior
    for i in range(len(list)):
        if list[i][0].is_loop: pass
        else:list[i][0].exterior = True
        if list[i][len(list[i])-1].is_loop: pass
        else:list[i][len(list[i])-1].exterior = True
    for i in range(len(list[0])):
        if list[0][i].is_loop: pass
        else:list[0][i].exterior = True
        if list[len(list)-1][i].is_loop: pass
        else:list[len(list)-1][i].exterior = True
    for count in range(10**3): # repeat a lot
        for i in range(1,len(list)-1):
            for j in range(1,len(list[i])-1):
                if list[i][j].is_loop or list[i][j].exterior: continue
                if list[i-1][j].exterior or list[i+1][j].exterior or list[i][j-1].exterior or list[i][j+1].exterior or list[i-1][j-1].exterior or list[i+1][j-1].exterior or list[i+1][j+1].exterior or list[i-1][j+1].exterior: list[i][j].exterior = True #this checks all 8 directions for an exterior tile
def floodFillInterior():
    # loop 1: get all edges marked as interior.
    # walk right and left marking all nearby to interior as interior
    for count in range(10**3): # repeat a lot
        for i in range(1,len(list)-1):
            for j in range(1,len(list[i])-1):
                if list[i][j].is_loop or list[i][j].interior: continue
                if list[i-1][j].interior or list[i+1][j].interior or list[i][j-1].interior or list[i][j+1].interior : list[i][j].interior = True #this checks all 8 directions for an interior tile  
                #or list[i-1][j-1].interior or list[i+1][j-1].interior or list[i+1][j+1].interior or list[i-1][j+1].interior                
def partOneScore():
    highest = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            compare = list[i][j].distance
            if compare < 99999 and compare > highest:
                highest = compare
    return highest
def partTwoScore():
    highest = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j].interior:
                highest+=1
    return highest
list = parseList(file.readlines())
x,y =findIcon("S",False)
list[x][y].distance = 0
loopFromPos(x,y,False)
printMaze()
print(f"Highest score = {partOneScore()}")
floodFillExterior()
printMaze()
print()
x,y = findIcon("-",True)
loopFromPos(x,y,True)
floodFillInterior()
printMaze()
print(f"Possible Interiors = {partTwoScore()}")


print("done")




# Upper bound for interiors = 544, NOT 82

#if list[i-1][j].exterior or list[i+1][j].exterior or list[i][j-1].exterior or list[i][j+1].exterior: list[i][j].exterior = True