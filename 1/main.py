

digits =  [str(i) for i in range(0,10)]
digits_3 = ["one", "two",  "six"]
digits_4 = ["four", "five", "nine"]
digits_5 = ["three", "seven", "eight"]

mapper = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}


with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        first = None
        for idx, char in enumerate(line):
            three = ""
            four = ""
            five = ""
            if idx+3 <= len(line):
                three = line[idx:idx+3]
            if idx+4 <= len(line):
                four = line[idx:idx+4]
            if idx+5 <= len(line):
                five = line[idx:idx+5]
            if char in digits:
                if first is None:
                    first = char
                last = char
            elif three in digits_3:
                temp = mapper[three]
                if first is None:
                    first = temp
                last = temp
            elif four in digits_4:
                temp = mapper[four]
                if first is None:
                    first = temp
                last = temp
            elif five in digits_5:
                temp = mapper[five]
                if first is None:
                    first = temp
                last = temp
        number = int(first+last)
        sum += number
    print(sum)
