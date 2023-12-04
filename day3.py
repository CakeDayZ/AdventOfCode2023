file = open("D:\Python\CodeAdvent2023\day3_input.txt","r")
list = file.readlines()
list2 =[]
line = 0
score = 0
gear_list = [[0,0,0,0]]
for i in list:
    list2.append( i.rstrip())
list = list2
line_len = len(list[0]) -1
bottom_line = len(list) -1
def detection(line,lower,upper,numbor):
    near = 0
    #print(line,lower,upper)
    line_low = line > 0
    line_high = line < bottom_line
    row_low = lower > 0
    row_high = upper < line_len
    if line_low: #Top
        for i in range(lower,upper):
            if checknum(line-1,i,numbor): near+=1
    if line_high: #Bottom
        for i in range(lower,upper):
            if checknum(line+1,i,numbor): near+=1
    if row_low: #Left
        if checknum(line,lower-1,numbor): near +=1
    if row_high:  #Right
        if checknum(line,upper,numbor): near +=1
    if line_low and row_low: #Top Left
        if checknum(line-1,lower-1,numbor): near +=1 
    if line_low and row_high:  #Top Right
        if checknum(line-1,upper,numbor): near +=1
    if line_high and row_low: #Bottom Left
        if checknum(line+1,lower-1,numbor): near +=1
    if line_high and row_high:  #Bottom Right
        if checknum(line+1,upper,numbor): near +=1
    return near
def checknum(x,y,numbor):
    if list[x][y] == "*": 
        gear_stats = [x,y,1,numbor]
        match = False
        for i in gear_list:
            if i[0] == x and i[1] == y:
                match = True
                if not i[3:].count(numbor):
                    i[2] = i[2] + 1
                    i.append(numbor)
                #print(f"sus {gear_stats}")
        if not match: gear_list.append(gear_stats)
        return True
    if not list[x][y] ==  "." and not list[x][y].isnumeric(): return True
    return False   
for i in list: # ...678...
    print(i)
    j = 0
    while j < line_len:
        if i[j].isnumeric():
            lower = j
            while i[j].isnumeric(): 
                j+=1
                if j  == line_len +1 : break
            upper = j
            numbor = int(i[lower:upper])
            if detection(line,lower,upper,numbor): 
                score += numbor
                #print(f"good number! {numbor}")
            #else: print(f"bad number! {numbor}")
        j+=1
    line +=1
    
print(f"Score is {score}")
score2 = 0
for i in gear_list:
    if i[2] == 2:
        mult = 1
        for j in i[3:]:
            mult = mult * j
        print(mult)
        score2+=mult
print(f"Gear Ratios Sum: {score2}")
#Part 1 Score is higher than 542978

#Take the input from good_gear_list then use that to reverse engineer all the nearby numbers accurately
# OR refactor. Make this into a gear-specific detection function that can do that easily.
# OR in the normal detection code, add a thing when a gear is detected - it adds the gear to a list, and that list also stores the numbers of nearby things. EG 678 detects a gear. Stores gear location of 1,5 and 678,
# and +1 near. On each gear find double check to see if its in list. If yes than just update thingy. 
# MAXIMUM calls is only like 3200. 