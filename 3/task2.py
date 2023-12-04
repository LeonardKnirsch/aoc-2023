ints = [str(i) for i in range(10)]
result = 0

def right_expand(data,j):
    number = int(data[j])
    if data[j+1] != ".":
        number = number * 10 + int(data[j+1])
        if data[j+2] != ".":
            number = number * 10 + int(data[j+2])
    return number

def left_expand(data,j):
    number = int(data[j])
    if data[j-1] != ".":
        number = number + int(data[j-1])*10
        if data[j-2] != ".":
            number = number + int(data[j-2])*100
    return number

def check_row(data,j):
    sol = []
    if data[j] in ints:
        if data[j-1] not in ints:
            sol.append(right_expand(data,j))
        elif data[j+1] not in ints:
            sol.append(left_expand(data,j))
        else:
            sol.append(right_expand(data,j-1))
    elif data[j-1] in ints:
        sol.append(left_expand(data,j-1))
    if data[j+1] in ints and not data[j] in ints:
        sol.append(right_expand(data,j+1))
    return sol

with open("input.txt", "r") as file:
    data = [["."]*3+[char for char in line.rstrip()]+["."]*3 for line in file]
    row = [146*["."]]
    data = 3*row + data + 3*row
    for i in range(146):
        for j in range(146):
            if data[i][j] != "." and data[i][j] not in ints and data[i][j]!="*":
                data[i][j] = "."
    for i in range(146):
        for j in range(146):
            if data[i][j] == "*":
                sols = []
                if data[i][j-1] in ints:
                    sols.append(left_expand(data[i],j-1))
                if data[i][j+1] in ints:
                    sols.append(right_expand(data[i],j+1))
                below = check_row(data[i+1],j)
                if below:
                    for x in below:
                        sols.append(x)
                above = check_row(data[i-1],j)
                if above:
                    for x in above:
                        sols.append(x)
                if len(sols) == 2:
                    result += sols[0]*sols[1]
                


                
                
print(result)
