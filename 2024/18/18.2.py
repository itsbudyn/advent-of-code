from copy import deepcopy

def main():
    with open("2024/18/18.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    
    maze = []
    width, height = 71, 71
    startpos, endpos = (1, 1), (width, height) 
    vertBorder = list("#"*(width+2))
    for y in range(height): maze.append(list("#"+width*"."+"#"))
    maze.insert(0, vertBorder)
    maze.append(vertBorder)

    for coord in range(1024):
        coordArray = list(map(int, text.pop(0).split(",")))
        maze[coordArray[1]+1][coordArray[0]+1] = "#"

    points_visited = set()
    paths = [[startpos]]
    lastPopped = ""

    while paths:
        path = paths[0]
        lastpos = path[-1]
        del paths[0]
        newpaths = []

        for nextpos in ((lastpos[0], lastpos[1]-1), (lastpos[0]+1, lastpos[1]), (lastpos[0], lastpos[1]+1), (lastpos[0]-1, lastpos[1])):
            if maze[nextpos[1]][nextpos[0]] != "#" and nextpos not in path and nextpos not in points_visited:
                newpath = deepcopy(path)
                newpath.append(nextpos)
                points_visited.add(nextpos)
                if nextpos == endpos: 
                    while text:
                        lastPopped = text.pop(0)
                        coord = list(map(int, lastPopped.split(",")))
                        coord = (coord[0]+1, coord[1]+1)
                        maze[coord[1]][coord[0]] = "#"
                        if coord in newpath:
                            paths = [[startpos]]
                            points_visited = set()
                            newpaths = []
                            newpath = None
                            break
                    break
                elif newpath not in newpaths: newpaths.append(newpath)
        if newpaths:
            for newpath in newpaths: paths.append(newpath)
    return lastPopped

if __name__ == "__main__": print(main())