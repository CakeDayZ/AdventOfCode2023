file = open("D:\Python\CodeAdvent2023\day5_example.txt","r")
list = file.readlines()
def unpackSeeds(string):
    seeds = string.split()[1:]
    for i in seeds: 
        seeds[seeds.index(i)] = int(i)
    return seeds
# def moreSeeds(seeds):
    # seeds2 = []
    # for i in range(len(seeds)):
        # if (i+1) % 2:
            # base = seeds[i]
        # else:
            # range2 = seeds[i]
            # for i in range(range2):
                # seeds2.append(base+i)  
            # print(len(seeds2))
    # return seeds2
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
seeds = unpackSeeds(list[0])
#seeds = moreSeeds(seeds)  # Part Two
print(seeds)
locations_list = []
dictionary = ["seed-to-soil map:\n","soil-to-fertilizer map:\n","fertilizer-to-water map:\n","water-to-light map:\n","light-to-temperature map:\n","temperature-to-humidity map:\n","humidity-to-location map:\n"]
for i in range(7):
    locations_list.append(list.index(dictionary[i]))
score = 999999999
for i in seeds:
    score = min(doMapping(i),score)
print(score)

