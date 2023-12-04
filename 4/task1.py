result = 0
with open("input.txt", "r") as file:
    for line in file:
        x = line.rstrip()
        x = x.split(":")[1]
        winners, my_numbers = x.split("|")
        winners = winners.split(" ")
        winners =  [int(i) for i in winners if i!="" and i!=" "]
        my_numbers = my_numbers.split(" ")
        my_numbers = [int(i) for i in my_numbers if i!=""]
        counter = 0
        for number in my_numbers:
            if number in winners:
                counter += 1
        if counter > 0:
            result += 2**(counter-1)
print(result)
        