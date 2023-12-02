file = open("D:\Python\CodeAdvent2023\day2_input.txt","r")
list = file.readlines()
#max_red = 12
#max_green = 13
#max_blue = 14
score = 0
for i in list:
    #valid_games = True
    min_red = 0
    min_blue = 0
    min_green = 0
    i = i[:-1]
    splitter = i.split(": ")
    game_id = int(splitter[0].strip()[5:])
    game_sets = splitter[1].split("; ")
    for j in game_sets:
        games = j.split(", ")
        for k in games:
            num = int(k.split(" ")[0])
            color = k.split(" ")[1]
            if color == "green":
                if num >= min_green: min_green = num
            elif color =="red":
                if num >= min_red: min_red = num
            elif color =="blue":
                if num >= min_blue: min_blue = num
            else: print( "huh")
            '''
            if num > max_blue and color == "blue":
                valid_games = False
                break
            elif color == "green" and num > max_green:
                valid_games = False
                break
            elif color == "red" and num > max_red:
                valid_games = False
                break
            else: pass
        if not valid_games: break
        '''
    #print (min_blue*min_green*min_red)
    score += min_blue*min_green*min_red
    #print(game_id)  
    #if valid_games : score += game_id
    #print(game_sets)
print(f"Score: {score}.")
#answer less than 56011