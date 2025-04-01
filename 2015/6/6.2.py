def main():
    with open("6.txt","r",encoding="UTF-8") as f: text=f.readlines()

    lights = [[0 for i in range(1000)] for j in range(1000)]

    for i in text:
        instr = i.split(" ")
        start_xy = instr[-3].split(",")
        end_xy = instr[-1].split(",")

        range_x = list(range(int(start_xy[0]),int(end_xy[0])+1))
        range_y = list(range(int(start_xy[1]),int(end_xy[1])+1))

        if not range_x: range_x = [int(start_xy[0])]
        if not range_y: range_y = [int(start_xy[1])]

        match instr[0]:
            case "turn":
                if instr[1] == "on": option = 1
                else: option = -1
                for y in range_y:
                    for x in range_x: 
                        lights[y][x] += option
                        if lights[y][x] < 0: lights[y][x] = 0
            case "toggle":
                for y in range_y:
                    for x in range_x: lights[y][x] += 2

    lights_on = 0
    for i in lights:
        lights_on+=sum(i)

    return lights_on    

if __name__ == "__main__": print(main())