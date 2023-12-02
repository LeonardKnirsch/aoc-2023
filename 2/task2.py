result = 0
game_id = 0

with open("input.txt", "r") as file:
    for line in file:
        game_id += 1
        x = line.split(":")[1]
        draws = x.split(";")
        min_red = 0
        min_green = 0
        min_blue = 0
        
        for draw in draws:
            sortof = draw.split(",")
            for sort in sortof:
                _,count,color = sort.rstrip().split(" ")
                count = int(count)
                if color == "red":
                    min_red = max(min_red,count)
                elif color == "green":
                    min_green = max(min_green,count)
                elif color == "blue":
                    min_blue = max(min_blue,count)
        power = min_blue*min_green*min_red
        result += power
print(result)