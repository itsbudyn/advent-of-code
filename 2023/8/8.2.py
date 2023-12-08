import re

def getNextPoint(arr:list, pos:str, direction:str):
    for i in range(len(arr)):
        if arr[i][0] == pos:
            match direction:
                case "L": return arr[i][1][0]
                case "R": return arr[i][1][1] 

def isFinished(positions:list):
    for i in positions:
        if i[-1] != "Z": return False
    return True

def main():
    with open("2023/8/8.txt","r",encoding="UTF-8") as f: text=f.read().splitlines()

    route = text[0]
    direction_arr = text[2:]

    directions = []
    for i in direction_arr:
        arr = i.split("=")
        directions.append([arr[0][:-1],re.findall(r"[A-Z0-9]{3}",arr[1])])

    current_pos = []
    for i in directions:
        if i[0][-1] == "A": current_pos.append(i[0])

    steps = 0
    while True:
        for i in range(len(route)):
            for j in range(0,len(current_pos)-1,2):
                current_pos[j] = getNextPoint(directions, current_pos[j], route[i])
                current_pos[j+1] = getNextPoint(directions, current_pos[j+1], route[i])
                steps+=1
                if isFinished(current_pos): return steps

if __name__ == "__main__": print(main())