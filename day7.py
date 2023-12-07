file = open("D:\Python\CodeAdvent2023\day7_input.txt","r")
list = file.readlines()
partTwo = True
max = len(list)
hands =[]
bids = []
ranks = []
if partTwo: high_cards = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
else: high_cards = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
def parseHand(input):
    hands.append(input.split()[0])
    bids.append(int(input.split()[1]))
    ranks.append(1)
    return input.split()[0]
def compareHands(hand1,hand2): # return true if hand1 is better
    valOne = handType(hand1)
    valTwo = handType(hand2)
    if not valOne == valTwo : return valOne > valTwo
    for i in range(len(hand1)):
        if not hand1[i] == hand2[i]:
            for j in high_cards:
                if hand1[i] == j: return True
                if hand2[i] == j: return False
def handType(input):
    counts = []
    jokers = 0
    for i in input:
        counts.append(input.count(i))
        if partTwo and i == "J" : jokers+=1
    if counts.count(5) : return 7
    if counts.count(4) : 
        if jokers: return 7
        return 6
    if counts.count(3) and counts.count(2): 
        if jokers: return 7
        return 5
    if counts.count(3) : 
        if jokers: return 6
        return 4
    if counts.count(2) == 4: # if 2 jokers return 6, if 1 joker return 5 else 3
        if jokers: return 4 + jokers
        return 3
    if counts.count(2) : 
        if jokers: return 4
        return 2
    return 1+jokers
def stupidSort(): #finds the rank of the newest card in the list, by comparing all cards and +1 to winner.
    target = hands[-1]
    target_index = len(hands)-1
    for i in hands:
        if i == target: continue
        if compareHands(target,i): ranks[target_index]+=1
        else: ranks[hands.index(i)]+=1
for i in list:
    parseHand(i)
    stupidSort()
hands2 = []
bids2 = []
for i in range(1,max+1): # reorder the lists to get them in actual order not just logical
    new_index = ranks.index(i)
    hands2.append(hands[new_index])
    bids2.append(bids[new_index])
hands = hands2
bids = bids2
totalScore = 0
for i in range(max):
    totalScore+= bids[i]*(i+1)
print(f"Score: {totalScore}")
#for i in range(max): #print all hands/bids formatted
#    print(f"{hands[i]} {bids[i]} ")
