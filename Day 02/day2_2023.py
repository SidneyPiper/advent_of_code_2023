with open('input.txt') as f:
    lines = f.readlines()

def starOne():
    game = []
    for i, line in enumerate(lines):
        possible = True

        line = line.split(":")[1]
        line = line.replace("\n", "")
        line = line.split(";")
        
        for set in line:
            set = set.split(",")
            for x in set:
                x = x[1:].split(" ")
                if x[1] == "red" and int(x[0]) > 12:
                    possible = False
                if x[1] == "green" and int(x[0]) > 13:
                    possible = False
                if x[1] == "blue" and int(x[0]) > 14:
                    possible = False
        
        if possible:
            game.append(i + 1)

    print(sum(game))


def starTwo():
    game = []
    result = 0

    for i, line in enumerate(lines):
        game.append({"red": 0, "green": 0, "blue": 0})
        line = line.split(":")[1]
        line = line.replace("\n", "")
        line = line.split(";")
        
        for set in line:
            set = set.split(",")
            for x in set:
                x = x[1:].split(" ")
                if x[1] == "red" and int(x[0]) > game[i]["red"]:
                    game[i]["red"] = int(x[0])
                if x[1] == "green"  and int(x[0]) > game[i]["green"]:
                    game[i]["green"] = int(x[0])
                if x[1] == "blue" and int(x[0]) > game[i]["blue"]:
                    game[i]["blue"] = int(x[0])
                
        result += game[i]["red"] * game[i]["green"] * game[i]["blue"]

    print(result)

starTwo()