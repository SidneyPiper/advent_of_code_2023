with open('input.txt') as f:
    lines = f.readlines()

def starOne():
    numbers = []

    for line in lines:
        first = last = ""

        for x in line:
            if x.isdigit():
                first = x
                break

        for x in reversed(line):
            if x.isdigit():
                last = x
                break

        numbers.append(int(first + last))  

    print(sum(numbers))

def starTwo():
    for i in range(len(lines)):
        lines[i] = lines[i].replace("one", "o1e")
        lines[i] = lines[i].replace("two", "t2o")
        lines[i] = lines[i].replace("three", "t3e")
        lines[i] = lines[i].replace("four", "f4r")
        lines[i] = lines[i].replace("five", "f5e")
        lines[i] = lines[i].replace("six", "s6x")
        lines[i] = lines[i].replace("seven", "s7n")
        lines[i] = lines[i].replace("eight", "e8t")
        lines[i] = lines[i].replace("nine", "n9e")
    
    starOne()


starTwo()