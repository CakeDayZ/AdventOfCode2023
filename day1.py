file = open("day1_input.txt","r")
list = file.readlines()
calibration = 0
#digitlist = ["1","2","3","4","5","6","7","8","9"] # Part One
digitlist = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"] # Part Two
for i in list:
    high = 0
    low = 64
    high_val = 0
    low_val = 0
    for j in digitlist:
        digit_location = i.find(j)
        if digit_location > -1:
            if digit_location <= low: 
                low = digit_location
                low_val = digitlist.index(j) % 9 + 1
            if digit_location >= high: 
                high = digit_location
                high_val = digitlist.index(j) % 9 + 1
    for j in digitlist:
        digit_location = i.rfind(j)
        if digit_location > -1:
            if digit_location < low: 
                low = digit_location
                low_val = digitlist.index(j) % 9 + 1
            if digit_location > high: 
                high = digit_location
                high_val = digitlist.index(j) % 9 + 1  
    val = low_val * 10 + high_val
    calibration+=val
print(f"Total Calibration: {calibration}.")