id_sum = 0
game_id = 0
red_limit = 12
green_limit = 13
blue_limit = 14
with open("input.txt", "r") as file:
    for line in file:
        game_id += 1
        x = line.split(":")[1]
        draws = x.split(";")
        valid = True
        for draw in draws:
            sortof = draw.split(",")
            for sort in sortof:
                _,count,color = sort.rstrip().split(" ")
                if color == "red" and int(count) > 12:
                    valid = False
                elif color == "green" and int(count) > 13:
                    valid = False
                elif color == "blue" and int(count) > 14:
                    valid = False
                if not valid:
                    break
        if valid:
            id_sum += game_id
print(id_sum)