def main():
    with open("2024/14/14.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")

    robots = {}
    seconds = 0
    width, height = 101, 103

    for robot in range(len(text)):
        robotData = text[robot].split(" ")
        robots[robot] = {"position":robotData[0][2:].split(","), "velocity":robotData[1][2:].split(",")}
        robots[robot]["position"] = list(map(int, robots[robot]["position"]))
        robots[robot]["velocity"] = tuple(map(int, robots[robot]["velocity"]))

    while True:
        for robot in list(robots.keys()):
            robots[robot]["position"][0] += robots[robot]["velocity"][0]
            robots[robot]["position"][1] += robots[robot]["velocity"][1]
            robots[robot]["position"][0] %= width
            robots[robot]["position"][1] %= height
        display = [["." for x in range(width)] for y in range(height)]
        seconds += 1

        positions = set()
        for robot in robots.values():
            positions.add(tuple(robot["position"]))

        potentialTree = False
        for position in list(positions):
            if (
                not potentialTree and
                2 < position[0] < width - 3 and 
                position[1] < height - 3 and
                (position[0], position[1] + 1) in positions and
                (position[0], position[1] + 2) in positions and
                (position[0] - 1, position[1] + 1) in positions and
                (position[0] + 1, position[1] + 1) in positions and
                (position[0] - 2, position[1] + 2) in positions and
                (position[0] - 1, position[1] + 2) in positions and
                (position[0] + 1, position[1] + 2) in positions and
                (position[0] + 2, position[1] + 2) in positions
            ): potentialTree = True
            
        if potentialTree:
            for position in list(positions):
                display[position[1]][position[0]] = "#"
            for i in display: 
                for j in i: print(j, end="")
                print()
            return seconds

if __name__ == "__main__": print(main())