def main():
    with open("2024/14/14.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")

    robots = {}
    width, height = 101, 103

    for robot in range(len(text)):
        robotData = text[robot].split(" ")
        robots[robot] = {"position":robotData[0][2:].split(","), "velocity":robotData[1][2:].split(",")}
        robots[robot]["position"] = list(map(int, robots[robot]["position"]))
        robots[robot]["velocity"] = tuple(map(int, robots[robot]["velocity"]))

    for seconds in range(100):
        for robot in list(robots.keys()):
            robots[robot]["position"][0] += robots[robot]["velocity"][0]
            robots[robot]["position"][1] += robots[robot]["velocity"][1]

    for robot in list(robots.keys()):
        robots[robot]["position"][0] %= width
        robots[robot]["position"][1] %= height

    quadrants = [0, 0, 0, 0]
    hHalf, vHalf = width // 2, height // 2
    for robot in robots.values():
        position = robot["position"]
        if position[0] < hHalf and position[1] < vHalf: quadrants[0]+=1
        elif position[0] > hHalf and position[1] < vHalf: quadrants[1]+=1
        elif position[0] > hHalf and position[1] > vHalf: quadrants[2]+=1
        elif position[0] < hHalf and position[1] > vHalf: quadrants[3]+=1

    return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]

    

if __name__ == "__main__": print(main())