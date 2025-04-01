def main():
    with open("2024/15/15.txt","r",encoding="UTF-8") as f: text = f.read().split("\n\n")

    result = 0
    currentPos = False
    maze = text[0].split("\n")
    maze = list(map(list, maze))

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
            case "O":
                match move:
                    case "^" | "v":
                        for search_y in searchRange:
                            match maze[search_y][currentPos[0]]:
                                case "#": break
                                case ".":
                                    maze[search_y][currentPos[0]] = "O"
                                    maze[nextpos[1]][nextpos[0]] = "@"
                                    maze[currentPos[1]][currentPos[0]] = "."
                                    currentPos = nextpos
                                    break
                    case "<" | ">":
                        for search_x in searchRange:
                            match maze[currentPos[1]][search_x]:
                                case "#": break
                                case ".":
                                    maze[currentPos[1]][search_x] = "O"
                                    maze[nextpos[1]][nextpos[0]] = "@"
                                    maze[currentPos[1]][currentPos[0]] = "."
                                    currentPos = nextpos
                                    break
        if False:
            for i in maze:
                for j in i: print(j, end="")
                print()
            input(move)
    
    for y in range(1, len(maze)-1):
        for x in range(1, len(maze[y])-1):
            if maze[y][x] == "O": result+= 100 * y + x
    return result
    

if __name__ == "__main__": print(main())