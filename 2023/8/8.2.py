import re
from math import lcm

def getNextPoint(arr:list, pos:str, direction:str):
    for i in arr:
        if i[0] == pos:
            match direction:
                case "L": return i[1][0]
                case "R": return i[1][1] 

def main():
    with open("8.txt","r",encoding="UTF-8") as f: text=f.read().splitlines()

    route = text[0]
    direction_arr = text[2:]

    directions = []
    current_pos = []

    for i in direction_arr:
        arr = i.split("=")
        if arr[0][:-1][-1] == "A": current_pos.append(arr[0][:-1])
        directions.append([arr[0][:-1],re.findall(r"[A-Z0-9]{3}",arr[1])])

    del direction_arr

    loop_steps = [0 for i in current_pos]

    for j in range(len(current_pos)): 
        steps = 0
        hit_loop = False
        while not hit_loop:
            for i in route:
                current_pos[j] = getNextPoint(directions, current_pos[j], i)
                steps+=1
                if current_pos[j][-1] == "Z":
                    loop_steps[j] = steps
                    hit_loop = True
                if hit_loop: break

    return lcm(*loop_steps)

if __name__ == "__main__": print(main())