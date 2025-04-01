import re

def getNextPoint(arr:list, pos:str, direction:str):
    for i in range(len(arr)):
        if arr[i][0] == pos:
            match direction:
                case "L": return arr[i][1][0]
                case "R": return arr[i][1][1] 

def main():
    with open("8.txt","r",encoding="UTF-8") as f: text=f.read().splitlines()

    route = text[0]
    direction_arr = text[2:]

    directions = []
    for i in direction_arr:
        arr = i.split("=")
        directions.append([arr[0][:-1],re.findall(r"[A-Z]{3}",arr[1])])

    current_pos = "AAA"
    steps = 0
    while current_pos != "ZZZ":
        for i in route:
            current_pos = getNextPoint(directions, current_pos, i)
            steps+=1

    return steps

if __name__ == "__main__": print(main())