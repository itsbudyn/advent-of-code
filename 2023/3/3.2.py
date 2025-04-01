import re

def horizontalNumSearch(lines, starty:int, startx:int, left:bool):
    number=""
    match left:
        case True: coords = range(startx-1,-1,-1)
        case False: coords = range(startx+1,len(lines[starty]))

    for k in coords:
        if re.match(r"[0-9]",lines[starty][k]): number+=lines[starty][k]
        else: break

    if number:
        match left:
            case True: return number[::-1]
            case False: return number
    else: return None


def main():
    with open("3.txt","r",encoding="UTF-8") as f: text = f.read()
    lines = text.splitlines()

    gear_ratios = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            gears = []
            if lines[i][j] == "*":
                # HORIZONTAL
                left = horizontalNumSearch(lines, i, j, True)
                right = horizontalNumSearch(lines, i, j, False)

                if left: gears.append(int(left))
                if right: gears.append(int(right))
      
                # UP
                left, middle, right = "", "", ""
                if i > 0:
                    if re.match(r"[0-9]",lines[i-1][j]): middle = lines[i-1][j]
                    left = horizontalNumSearch(lines, i-1, j, True)
                    right = horizontalNumSearch(lines, i-1, j, False)

                    if not left: left=""
                    if not right: right=""

                    if middle: gears.append(int(left+middle+right))
                    else: 
                        if left: gears.append(int(left))
                        if right: gears.append(int(right))

                # DOWN
                left, middle, right = "", "", ""
                if i < len(lines)-1:
                    if re.match(r"[0-9]",lines[i+1][j]): middle = lines[i+1][j]
                    left = horizontalNumSearch(lines, i+1, j, True)
                    right = horizontalNumSearch(lines, i+1, j, False)

                    if not left: left=""
                    if not right: right=""

                    if middle: gears.append(int(left+middle+right))
                    else: 
                        if left: gears.append(int(left))
                        if right: gears.append(int(right))

                if len(gears) == 2:
                    ratio = 1
                    for g in gears: ratio*=g
                    gear_ratios.append(ratio)
    return sum(gear_ratios)

if __name__ == "__main__": print(main())