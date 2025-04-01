from copy import deepcopy

def getBearing(point1:tuple, point2:tuple):
    if   point1[0] == point2[0] and point1[1] < point2[1]: return 180
    elif point1[0] == point2[0] and point1[1] > point2[1]: return 0
    elif point1[1] == point2[1] and point1[0] < point2[0]: return 90
    elif point1[1] == point2[1] and point1[0] > point2[0]: return 270

def getDistAndSpins(path:list, connections:dict):
    dist = 0
    spins = 0
    bearing = 90
    for coord in range(len(path)-1):
        dist += connections[path[coord]][path[coord+1]]
        newBearing = getBearing(path[coord], path[coord+1])
        if bearing != newBearing:
            spins += 1
            bearing = newBearing
    return dist, spins

def main():
    with open("2024/16/16.txt","r",encoding="UTF-8") as f: maze = f.read().split("\n")
    maze = list(map(list, maze))
    startpos, endpos = (), ()
    points = set()
    connections = {}

    for y in range(1, len(maze)-1):
        for x in range(1, len(maze[y])-1):
            match maze[y][x]:
                case "E": 
                    endpos = (x, y)
                    maze[y][x] = "."
                case "S": 
                    startpos = (x, y)
                    maze[y][x] = "."
            if maze[y][x] == ".": points.add((x,y))

    for point in points: connections[point] = {}
    for point in points:
        for checkedPoint in ((point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1), (point[0] - 1, point[1])): 
            if checkedPoint in points: connections[point][checkedPoint] = 1

    paths_found = []
    paths = [[startpos]]
    nodesVisited = {}

    while paths:
        print(len(paths))
        newpaths = []
        path = paths[0]
        lastpos = path[-1]

        del paths[0]
        for nextPos in connections[lastpos].keys():
            if nextPos not in path:
                newpath = deepcopy(path)
                newpath.append(nextPos)
                if nextPos == endpos:
                    if newpath not in paths_found: paths_found.append(newpath)
                elif newpath not in newpaths: 
                    dist, spins = getDistAndSpins(newpath, connections)
                    if nextPos not in nodesVisited.keys() or spins <= nodesVisited[nextPos][1] or dist <= nodesVisited[nextPos][0]:
                        if nextPos in nodesVisited.keys() and (spins < nodesVisited[nextPos][1] or dist < nodesVisited[nextPos][0]):
                            indexes_to_remove = set()
                            for i in range(len(newpaths)):
                                if nextPos in newpaths[i]: indexes_to_remove.add(i)
                            if indexes_to_remove:
                                for index in indexes_to_remove: newpaths.pop(index)
                        nodesVisited[nextPos] = (dist, spins)
                        newpaths.append(newpath)
                
        if newpaths:
            for newpath in newpaths: 
                if newpath not in paths: paths.append(newpath)

    min_result = 999999999999
    resultDict = {}
    print(len(paths_found))
    for path in paths_found:
        distance, spins = getDistAndSpins(path, connections)
        result = distance + 1000*spins
        if result < min_result: 
            if result not in resultDict.keys(): resultDict[result] = [path]
            else: resultDict[result].append(path)

    min_result = min(resultDict.keys())
    commonSet = set(resultDict[min_result][0])
    for path in range(1, len(resultDict[min_result])): commonSet |= set(resultDict[min_result][path])

    print(min_result)
    return len(commonSet)

if __name__ == "__main__": print(main())