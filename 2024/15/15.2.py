from copy import deepcopy

def main():
    with open("2024/15/15.txt","r",encoding="UTF-8") as f: text = f.read().split("\n\n")

    result = 0
    currentPos = False
    maze = text[0].split("\n")
    maze = list(map(list, maze))
    maze[0] = maze[0]*2
    maze[-1] = maze[-1]*2
    for y in range(1, len(maze)-1):
        newLine = []
        for x in range(len(maze[y])):
            match maze[y][x]:
                case "#": newLine += ["#"] + ["#"]
                case "O": newLine += ["["] + ["]"]
                case ".": newLine += ["."] + ["."]
                case "@": newLine += ["@"] + ["."]
        maze[y] = newLine

    for y in range(len(maze)):
        if currentPos: break
        for x in range(len(maze[y])):
            if maze[y][x] == "@":
                currentPos = (x, y)
                break

    moves = "".join(i for i in text[1].split("\n"))    
    for move in moves:
        match move:
            case "^": 
                nextpos = (currentPos[0], currentPos[1] - 1)
                searchRange = range(currentPos[1] - 2, 0, -1)
            case ">": 
                nextpos = (currentPos[0] + 1, currentPos[1])
                searchRange = range(currentPos[0] + 2, len(maze[currentPos[1]]) - 1)
            case "v": 
                nextpos = (currentPos[0], currentPos[1] + 1)
                searchRange = range(currentPos[1] + 2, len(maze) - 1)
            case "<": 
                nextpos = (currentPos[0] - 1, currentPos[1])
                searchRange = range(currentPos[0] - 2, 0, -1)

        match maze[nextpos[1]][nextpos[0]]:
            case ".":
                maze[nextpos[1]][nextpos[0]] = "@"
                maze[currentPos[1]][currentPos[0]] = "."
                currentPos = nextpos
            case "[" | "]":
                match move:
                    case "^" | "v":
                        nextStep = 1 if currentPos < nextpos else -1
                        for search_y in searchRange:
                            match maze[search_y][currentPos[0]]:
                                case "#": break
                                case ".":
                                    boxes_to_move = set()
                                    match maze[nextpos[1]][nextpos[0]]:
                                        case "[": boxes_to_move.add(((nextpos[0], nextpos[1]), (nextpos[0] + 1, nextpos[1])))
                                        case "]": boxes_to_move.add(((nextpos[0] - 1, nextpos[1]), (nextpos[0], nextpos[1])))

                                    while True:
                                        oldLen = len(boxes_to_move)
                                        for box in list(boxes_to_move):
                                            for coord in box:
                                                match maze[coord[1] + nextStep][coord[0]]:
                                                    case "#":
                                                        boxes_to_move.add(-1)
                                                        break
                                                    case "[": boxes_to_move.add(((coord[0], coord[1] + nextStep), (coord[0] + 1, coord[1] + nextStep)))
                                                    case "]": boxes_to_move.add(((coord[0] - 1, coord[1] + nextStep), (coord[0], coord[1] + nextStep)))

                                        if oldLen == len(boxes_to_move) or -1 in boxes_to_move: break
                                    if -1 in boxes_to_move: break

                                    newMaze = deepcopy(maze)
                                    abort = False
                                    for box in boxes_to_move:
                                        newMaze[box[0][1]][box[0][0]] = "."
                                        newMaze[box[0][1]][box[1][0]] = "."
                                    for box in boxes_to_move:
                                        if maze[box[0][1] + nextStep][box[0][0]] == "#" or maze[box[0][1] + nextStep][box[1][0]] == "#":
                                            abort = True
                                            break
                                        else: 
                                            newMaze[box[0][1] + nextStep][box[0][0]] = "["
                                            newMaze[box[0][1] + nextStep][box[1][0]] = "]"
                                    if not abort: 
                                        maze = deepcopy(newMaze)
                                        maze[nextpos[1]][nextpos[0]] = "@"
                                        maze[currentPos[1]][currentPos[0]] = "."
                                        currentPos = nextpos
                                    break

                    case "<" | ">":
                        for search_x in searchRange:
                            match maze[currentPos[1]][search_x]:
                                case "#": break
                                case ".":
                                    maze[nextpos[1]][nextpos[0]] = "@"
                                    maze[currentPos[1]][currentPos[0]] = "."
                                    for rep_x in range(currentPos[0], search_x, 1 if search_x - currentPos[0] > 0 else - 1):
                                        if maze[currentPos[1]][rep_x] == "]": maze[currentPos[1]][rep_x] = "["
                                        elif maze[currentPos[1]][rep_x] == "[": maze[currentPos[1]][rep_x] = "]"
                                    match move:
                                        case "<": maze[currentPos[1]][search_x] = "["
                                        case ">": maze[currentPos[1]][search_x] = "]"
                                    currentPos = nextpos
                                    break

    for y in range(1, len(maze) - 1):
        skip = False
        for x in range(2, len(maze[y]) - 3):
            if not skip and maze[y][x] == "[": 
                dist_x, dist_y = x, y
                result += 100 * dist_y + dist_x
                skip = True
            elif skip: skip = False
    return result

if __name__ == "__main__": print(main())