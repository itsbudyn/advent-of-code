def main():
    with open("2024/20/20.txt","r",encoding="UTF-8") as f: maze = list(map(list, f.read().split("\n")))
    cheats_1, cheats_2 = {}, {}
    removableWalls = set()

    for y in range(1, len(maze)-1):
        for x in range(len(maze[y])-1):
            match maze[y][x]:
                case "E": endpos = (x, y)
                case "S": startpos = (x, y)
                case "#":
                    if (maze[y][x-1] != "#" and maze[y][x+1] != "#"): removableWalls.add(((x-1, y), (x+1, y)))
                    elif (maze[y-1][x] != "#" and maze[y+1][x] != "#"): removableWalls.add(((x, y-1), (x, y+1)))

    path = [startpos]
    while path[-1] != endpos:
        lastpos = path[-1]
        for nextpos in {(lastpos[0], lastpos[1] - 1), (lastpos[0] + 1, lastpos[1]), (lastpos[0], lastpos[1] + 1), (lastpos[0] - 1, lastpos[1])}:
            if maze[nextpos[1]][nextpos[0]] != "#" and nextpos not in path:
                path.append(nextpos)
                break

    for wall in removableWalls:
        noclipBegin, noclipEnd = path.index(wall[0]), path.index(wall[1])
        timeSaved = abs(noclipBegin - noclipEnd) - 2
        if timeSaved not in cheats_1.keys(): cheats_1[timeSaved] = 1
        else: cheats_1[timeSaved] += 1

    cheatCount = 0
    for i in sorted(cheats_1.keys()): 
        if i >= 100: cheatCount += cheats_1[i]
    print("Part 1:",cheatCount)

    searchRange = 20
    for point in path:
        noclipBegin = path.index(point)
        for y in range(searchRange + 1):
            for x in range(point[0] - searchRange + y, point[0] + searchRange - y + 1):
                for searchPoint in set(((x, point[1]+y), (x, point[1]-y))):
                    if searchPoint in path: 
                        realDist = abs(point[0] - searchPoint[0]) + abs(point[1] - searchPoint[1])
                        noclipEnd = path.index(searchPoint)
                        if noclipEnd > noclipBegin: 
                            timeSaved = noclipEnd - noclipBegin - realDist
                            if timeSaved not in cheats_2.keys(): cheats_2[timeSaved] = 1
                            else: cheats_2[timeSaved] += 1

    cheat2Count = 0
    for i in sorted(cheats_2.keys()):
        if i >= 100: cheat2Count += cheats_2[i]
    print("Part 2:",cheat2Count)

    return cheatCount, cheat2Count

if __name__ == "__main__": print(main())