def main():
    with open("12.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    regions = []
    text = list(map(list, text))

    for y in range(len(text)):
        for x in range(len(text[y])):
            if text[y][x] != ".":
                perimeter = 0
                regionIcon = text[y][x]
                points, points_checked = [], []
                points.append((x, y))
                while points:
                    newpoints = []
                    checkedPoint = points[0]
                    checked_x, checked_y = checkedPoint[0], checkedPoint[1]
                    del points[0]
                    points_checked.append(checkedPoint)

                    if                        checked_y > 0 and text[checked_y-1][checked_x] == regionIcon: newpoints.append((checked_x, checked_y-1))
                    if            checked_y < len(text) - 1 and text[checked_y+1][checked_x] == regionIcon: newpoints.append((checked_x, checked_y+1))
                    if                        checked_x > 0 and text[checked_y][checked_x-1] == regionIcon: newpoints.append((checked_x-1, checked_y))
                    if checked_x < len(text[checked_y]) - 1 and text[checked_y][checked_x+1] == regionIcon: newpoints.append((checked_x+1, checked_y))
                    perimeter += 4 - len(newpoints)
                    
                    for newpoint in newpoints:
                        if newpoint not in points and newpoint not in points_checked: points.append(newpoint)
                for point in points_checked: text[point[1]][point[0]] = "."

                regions.append(len(points_checked)*perimeter)

    return sum(regions)

if __name__ == "__main__": print(main())