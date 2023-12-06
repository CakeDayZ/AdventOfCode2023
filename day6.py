file = open("D:\Python\CodeAdvent2023\day6_input.txt","r")
part2 = False
list = file.readlines()
times = list[0].split()[1:]
count = len(times)
part2_times = ""
part2_dist = ""
for i in range(count):
    part2_times = part2_times + times[0]
    times.append(int(times[0]))
    times.pop(0)
if part2: times= int(part2_times)
distances= list[1].split()[1:]
print("----------------")
for i in range(count):
    part2_dist = part2_dist + distances[0]
    distances.append(int(distances[0]))
    distances.pop(0)
if part2: distances = int(part2_dist)
# i want to find all winning (not tying)times
# idea is to find min speed and maximum speed. All others between are assumed.
# Highest and lowest speed are same but flipped. Can find the other by time - max_speed
print(times)
print(distances)
scores = []
def testRace(speed,time,distance):
    actual_distance = (time-speed) * speed
    if actual_distance > distance: return True
    return False
if part2:
    find_max = True
    find_min = True
    min_speed = int(times/2)
    max_speed = int(times/2)
    buffer = times
    while find_max: # Binary search each half to find max, repeat with min
        avg = int((buffer+max_speed)/2)
        max_result = testRace(max_speed,times,distances)
        buffer_result = testRace(buffer,times,distances)
        avg_result = testRace(avg,times,distances)
        if buffer_result:
            max_speed = buffer
            buffer+=1000
        elif avg_result:
            max_speed = avg
        elif max_result:
            max_speed+=1
            new_buffer =int(buffer * .99)
            if new_buffer >= max_speed: buffer = new_buffer
            elif buffer-1500 >= max_speed: buffer-=1000
            else:buffer-=1
        elif testRace(max_speed-1,times,distances) and not max_result: 
            max_speed-=1
            find_max = False
            print("winner")
        print(f"loop Mspeed:{max_speed} Aspeed:{avg} Bspeed {buffer}")
    print(max_speed)
    min_speed = times-max_speed
    print(min_speed)
    scores.append(max_speed - min_speed + 1)
else:
    for i in range(count):
        time = times[i]
        distance = distances[i]
        min_speed = time
        max_speed = 1
        for j in range(time):
            if testRace(j,time,distance):
                if j >= max_speed: max_speed=j
        min_speed= time-max_speed
        scores.append(max_speed - min_speed + 1)
        print(f"Race {i}: Min={min_speed}, Max ={max_speed}, Score = {scores[i]}")
total_score = 1
for i in scores:
    total_score*=i
print(total_score)