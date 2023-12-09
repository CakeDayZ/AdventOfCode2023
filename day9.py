file = open("D:\Python\CodeAdvent2023\day9_input.txt","r")
list = file.readlines()
def parseInput(input):
    str_list = input.split()
    for i in range(len(str_list)):
        str_list[i] = int(str_list[i])
    return str_list
def recursiveSolver(input):
    diff_list = []
    diff_len = len(input)-1
    for i in range(diff_len):
        diff_list.append(input[i+1]-input[i])
    print(diff_list)
    if diff_list.count(0) < diff_len:
        if part_two: total = input[0] - recursiveSolver(diff_list)
        else: total = input[-1] + recursiveSolver(diff_list)
        return total
    print("end recursion")
    return input[0]
part_two = True
sum = 0
for i in list:
    result = []
    next_history = recursiveSolver(parseInput(i))
    #print(parseInput(i))
    #print(next_history)
    sum+=next_history
print(f"Total Sum: {sum}")