# first digit (alpha char) plus last digit results in 2 digit calibration value

# What is the sum of all the calibration values?

with open('input.txt') as lines:
    strings = [line for line in lines if line != "\n"]
cal_values = []
for string in strings:
    for char in string:
        if char.isdigit():
            digit1 = char
            break
    for char in string[::-1]:
        if char.isdigit():
            digit2 = char
            break
    cal_values.append(digit1 + digit2)
cal_values_int = [int(e) for e in cal_values]
result = sum(cal_values_int)
print(f"{result=}")


