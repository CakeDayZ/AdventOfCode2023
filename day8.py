def parseString(input):
    list2 = i.split()
    maps.append(list2[0])
    lefts.append(list2[2][1:4])
    rights.append(list2[3][0:3])
def useMapPartTwo(input): #this one isnt gonna work, over 21,700,000 steps and no answer
    current = input
    current_index = maps.index(current)
    steps = 0
    goLeft = nextPattern(pattern,steps)
    while not current[2] == "Z":
        if goLeft: current = lefts[current_index]    
        else: current = rights[current_index]
        current_index = maps.index(current)
        steps +=1
        goLeft = nextPattern(pattern,steps)
        if not steps%100000: print(steps,current,current_index)
    return steps
def nextPattern(pattern,pattern_index):
    pattern_index = pattern_index % len(pattern)
    if pattern[pattern_index] == "L":return True
    if pattern[pattern_index] == "R":return False
def useResults():
    # i used https://www.calculatorsoup.com/calculators/math/lcm.php after trying for 2 hours.
    return results
file = open("D:\Python\CodeAdvent2023\day8_input.txt","r")
list = file.readlines()
pattern = list[0].rstrip()
pattern_length = len(pattern)
maps= []
lefts =[]
rights= []
for i in list[2:]:
    parseString(i)
print(f"Part One Steps: {useMapPartTwo('AAA')}")
#Part Two
starting_ref = []
for i in maps: 
        if i[2] == "A": starting_ref.append(i)
print(starting_ref)
results = []
for i in starting_ref:
    results.append(useMapPartTwo(i))
print(f"Part Two Steps: {useResults()}")

# too high 33700215551376258894378011