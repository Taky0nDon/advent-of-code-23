# first digit (alpha char) plus last digit results in 2 digit calibration value

# What is the sum of all the calibration values?
spelled_nums = {"one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"
                }

with open('input.txt') as lines:
    strings = [line for line in lines if line != "\n"]
print(len(strings))
cal_values = []
test_result = 0
for string in strings:
    num_positions = {}
    print(f"{string=}")
    
    for spelled_num in spelled_nums:
        if spelled_num in string:
            spelled_num_position = int(string.find(spelled_num))
            right_spelled_num_pos = int(string.rfind(spelled_num))
            num_positions[spelled_num_position] = int(spelled_nums[spelled_num])
            num_positions[right_spelled_num_pos] = int(spelled_nums[spelled_num])

    for char in string:
        if char.isdigit():
            num_positions[string.find(char)] = int(char)
            num_positions[string.rfind(char)] = int(char)
#           break
#    for char in string[::-1]:
#        if char.isdigit():
#            digit2 = char
#            break
    first_app = num_positions[min([int(pos) for pos in num_positions.keys()])]
    last_app = num_positions[max([int(pos) for pos in num_positions.keys()])]
    print(f"{first_app=}, {last_app=}")

    concat_digits = str(first_app) + str(last_app)
    print(concat_digits)
    test_result += int(concat_digits)
    cal_values.append(concat_digits)
    
cal_values_int = [int(e) for e in cal_values]
print(cal_values_int)
result = sum(cal_values_int)
print(f"{len(cal_values_int)}")
print(f"{result=}, {test_result=}")


