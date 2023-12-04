ints = [str(i) for i in range(10)]
result = 0
with open("input.txt", "r") as file:
    data = [["."]+[char for char in line.rstrip()]+["."] for line in file]
    row = [142*["."]]
    data = row + data + row
    for i in range(142):
        for j in range(142):
            if data[i][j] != "." and data[i][j] not in ints:
                data[i][j] = "*"
    for i, x in enumerate(data):
        current_nr = 0
        for j, y in enumerate(x):
            if y in ints:
                if current_nr == 0:
                    start_j = j-1
                current_nr = int(y)+10*current_nr
            elif current_nr != 0:
                end_j = j+1
                start_i = i-1
                end_i = i+1

                
                rows = data[start_i:end_i+1]
                boundary = [row[start_j:end_j] for row in rows]
                boundary = [item for sublist in boundary for item in sublist]
                success = False
                for x in boundary:
                    if x == "*":
                        success = True
                if success:
                    result += current_nr
                current_nr = 0
print(result)
