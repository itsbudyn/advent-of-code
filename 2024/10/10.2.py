def main():
    with open("2024/10/10.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    paths = []
    paths_completed = []

    for y in range(len(text)):
        text[y] = list(map(int, text[y]))
        for x in range(len(text[0])):
            if text[y][x] == 0: paths.append([[x,y]])

    while len(paths):
        newpaths = []
        x, y = paths[0][-1][0], paths[0][-1][1]
        # up
        if y > 0 and text[y-1][x] - 1 == text[y][x]: newpaths.append(paths[0]+[[x, y-1]])
        # down
        if y < len(text)-1 and text[y+1][x] - 1 == text[y][x]: newpaths.append(paths[0]+[[x, y+1]])
        # left
        if x > 0 and text[y][x-1] - 1 == text[y][x]: newpaths.append(paths[0]+[[x-1, y]])
        # right
        if x < len(text[0])-1 and text[y][x+1] - 1 == text[y][x]: newpaths.append(paths[0]+[[x+1, y]])

        for i in newpaths:
            x, y = i[-1][0], i[-1][1]
            if text[y][x] == 9: paths_completed.append(i)
            else: paths.append(i)

        paths.pop(0)

    return len(paths_completed)

if __name__ == "__main__": print(main())