import random
file = open("D:\Python\CodeAdvent2023\day5_input.txt","r")
list = file.readlines()
def unpackSeeds(string):
    seeds = string.split()[1:]
    for i in seeds: 
        seeds[seeds.index(i)] = int(i)
    return seeds
def doMapping(input):
    for i in range(7):
        position = locations_list[i] + 1
        while list[position][0].isnumeric():
            nums = list[position].split()
            diff = input - int(nums[1])
            if diff >= 0 and diff < int(nums[2]):
                input = int(nums[0]) + diff
                break
            else: 
                position+=1
    return input
def reverseDoMapping(input):
    for i in range(6,-1,-1):
        position = locations_list[i] + 1
        while list[position][0].isnumeric():
            nums = list[position].split()
            diff = input - int(nums[0])
            if diff >= 0 and diff < int(nums[2]):
                input = int(nums[1]) + diff
                break
            else: 
                position+=1
    return input
def checkInSeeds(input):
    for i in range(0,len(seeds),2):
        if input >=seeds[i] and input < seeds[i]+seeds[i+1]: return True
    # for i in seeds:
        # if input == i: return True
    return False
seeds = unpackSeeds(list[0])
print(seeds)
locations_list = []
dictionary = ["seed-to-soil map:\n","soil-to-fertilizer map:\n","fertilizer-to-water map:\n","water-to-light map:\n","light-to-temperature map:\n","temperature-to-humidity map:\n","humidity-to-location map:\n"]
for i in range(7):
    locations_list.append(list.index(dictionary[i]))
score = 999999999
for i in seeds:
    score = min(doMapping(i),score)
print(score)
finished = False
executions = 0
counter = 1
upper_bound = 47909639
lower_bound = 13000000
while not finished:
    executions +=1
    if checkInSeeds(reverseDoMapping(upper_bound-counter)): 
        upper_bound = upper_bound-counter
        print(f"new upper bound of {upper_bound}")
        counter = 1
    else:
        counter+=1
    if not executions % 1000000: print(f"looped {executions} times...\nBetween {lower_bound} and {upper_bound}...")
print(f"Lowest possible score is {upper_bound}. By seed number {reverseDoMapping(upper_bound)}.")

#Part two was MESSY as fuck.

'''
while not finished:
    executions +=1
    rng = random.randint(lower_bound,upper_bound)
    if checkInSeeds(reverseDoMapping(rng)): 
        upper_bound = rng
        print(f"new upper bound of {upper_bound}")
        counter = 2
    else:
        rng = random.randint(upper_bound-counter,upper_bound-1)
        if checkInSeeds(reverseDoMapping(rng)):  
            upper_bound = rng
            print(f"new upper bound of {upper_bound}")
            counter = 2 
        else: counter +=1
        if checkInSeeds(reverseDoMapping(lower_bound)):
            upper_bound = lower_bound
        else: lower_bound+=1
    if upper_bound == lower_bound: finished = True
    if not executions % 1000000: print(f"looped {executions} times...\nBetween {lower_bound} and {upper_bound}...")
print(f"Lowest possible score is {upper_bound}. By seed number {reverseDoMapping(upper_bound)}.")
'''

 #226172555 is too high
    

