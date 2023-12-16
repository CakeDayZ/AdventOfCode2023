class Galaxy():
    def __init__(self,count,x,y):
        self.number = count
        self.x = x
        self.y = y
def parseList(input):
    list =[]
    for i in range(len(input)):
        list.append(input[i].rstrip()) 
    return list
def cosmicExpansion(partTwo):
    to_insert = []
    for i in range(len(list)-1,-1,-1):
        if list[i].count("#") <= 0:
            print(f"H add {i}")
            if partTwo:
                str = "O"*len(list[i])
                list[i]=str
            else: list.insert(i,list[i])
    for i in range(len(list[0].rstrip())-1,-1,-1):
        count = False
        for j in range(len(list)):
            if list[j][i] == "#": 
                count = True
                break
        if not count: 
            print(f"V add {i}")
            for j in range(len(list)):
                if partTwo:list[j] = list[j][:i]+ "O"+list[j][i+1:]
                else:list[j] = list[j][:i]+ "."+list[j][i:]
def printList():
    for i in list:
        print(i)
def printGalaxies():
    for i in galaxy_list:
        print(f"Num:{i.number}\tX:{i.x}\tY:{i.y}")
def printPairsList():
    for i in pairs_list:
        print(f"G1:{i[0]}\tG2:{i[1]}\tDist:{i[2]}")
def trackGalaxies():
    galaxy_list = []
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == "#":
                galaxy_list.append(Galaxy(len(galaxy_list)+1,i,j))
    return galaxy_list
def createPairsList():
    pairs_list = []
    for i in range(len(galaxy_list)-1):
        gal1 = galaxy_list[i]
        for j in galaxy_list[i+1:]:
         
            dist = getDistance(gal1,j)
            pairs_list.append([gal1.number,j.number,dist])
    return pairs_list
def getDistance(gal1,gal2):
    curr_x, dest_x = gal1.x, gal2.x
    curr_y, dest_y = gal1.y, gal2.y
    ex_mult = 1000000
    steps = 0
    while not curr_x == dest_x:
        if curr_x > dest_x: curr_x-=1
        if curr_x < dest_x: curr_x+=1
        if list[curr_x][curr_y] == "O": steps+=ex_mult-1
        steps+=1
    while not curr_y == dest_y:
        if curr_y > dest_y: curr_y-=1
        if curr_y < dest_y: curr_y+=1
        if list[curr_x][curr_y] == "O": steps+=ex_mult
        else:steps+=1
    return steps
def getScore():
    sum =0
    for i in pairs_list:
        sum+=i[2]
    return sum
file = open("D:\Python\CodeAdvent2023\day11_input.txt","r")
list = parseList(file.readlines())
cosmicExpansion(True)
galaxy_list = trackGalaxies()
printList()
#printGalaxies()
pairs_list = createPairsList()
print(getScore())
#printPairsList()