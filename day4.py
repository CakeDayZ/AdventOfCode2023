def stringToNumList(string,count):
    new_list = []
    for j in range(0,count,3):
        new_list.append (int(string[j:j+3].strip()))
    return new_list
def compareLists(win_list,check_list):
    matches = 0
    for i in win_list:
        for j in check_list:
            if i == j:
                matches +=1
                break
    '''part 1 stuff
    #if matches: score = 2**(matches-1)
    #else: score = 0
    #print(score)
    #return score '''
    return matches
file = open("D:\Python\CodeAdvent2023\day4_input.txt","r")
list = file.readlines()
#score = 0
match_list = []
copy_list = []
card_count =0
for i in list: 
    win_nums_string = i.split(":")[1].split("|")[0].rstrip()
    win_count = int(len(win_nums_string))
    win_nums_list = stringToNumList(win_nums_string,win_count)
    check_nums_string = i.split("|")[1].rstrip()
    check_count = int(len(check_nums_string))
    check_nums_list =stringToNumList(check_nums_string,check_count)
    #score +=compareLists(win_nums_list,check_nums_list) #part 1
    match_list.append(compareLists(win_nums_list,check_nums_list))
    copy_list.append(1)
    card_count +=1
#print(score) #part 1
#print(match_list)
#print(copy_list)
for i in range(card_count): 
    dupes = match_list[i]
    current = i +1
    while dupes > 0 and current < card_count:
        copy_list[current] += copy_list[i]
        dupes-=1
        current +=1
    #print(copy_list)
score2=0
for i in copy_list: score2+=i
print(score2)
