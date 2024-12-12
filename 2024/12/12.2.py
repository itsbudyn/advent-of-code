from copy import deepcopy

def isVertice(point:tuple, pointsArr: list):
    return (
        ((point[0], point[1] - 1) in pointsArr and (point[0] + 1, point[1]) in pointsArr) or
        ((point[0], point[1] + 1) in pointsArr and (point[0] + 1, point[1]) in pointsArr) or
        ((point[0], point[1] + 1) in pointsArr and (point[0] - 1, point[1]) in pointsArr) or
        ((point[0], point[1] - 1) in pointsArr and (point[0] - 1, point[1]) in pointsArr)
    )

def isSide(point:tuple, pointsArr: list):
    return (
        ((point[0] - 1, point[1]) in pointsArr and (point[0] + 1, point[1]) in pointsArr) or
        ((point[0], point[1] - 1) in pointsArr and (point[0], point[1] + 1) in pointsArr)
    )

def main():
    with open("12.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    result = 0
    text = list(map(list, text))
    dotsep = list(str("."*3*len(text[0])))
    enlarged_text = [dotsep]

    for line in text:
        enlarged_line = []
        for char in line: enlarged_line+=[".",char,"."]
        enlarged_text.append(enlarged_line)
        enlarged_text.append(dotsep)
        enlarged_text.append(dotsep)
    enlarged_text.pop(-1)

    enlarged_text_org = deepcopy(enlarged_text)

    for y in range(1,len(enlarged_text),3):
        for x in range(1,len(enlarged_text[y]),3):
            if enlarged_text[y][x] != ".":
                perimeter = 0
                regionIcon = enlarged_text[y][x]
                points, points_checked, sidePoints = [], [], set()
                points.append((x, y))
                while points:
                    newpoints = []
                    checkedPoint = points[0]
                    checked_x, checked_y = checkedPoint[0], checkedPoint[1]
                    del points[0]
                    points_checked.append(checkedPoint)

                    if checked_y > 1 and enlarged_text[checked_y-3][checked_x] == regionIcon: newpoints.append((checked_x, checked_y-3))
                    else:
                        sidePoints.add((checked_x, checked_y-1))
                        sidePoints.add((checked_x-1, checked_y-1))
                        sidePoints.add((checked_x+1, checked_y-1))
                        
                    if checked_y < len(enlarged_text) - 2 and enlarged_text[checked_y+3][checked_x] == regionIcon: newpoints.append((checked_x, checked_y+3))
                    else:
                        sidePoints.add((checked_x, checked_y+1))
                        sidePoints.add((checked_x-1, checked_y+1))
                        sidePoints.add((checked_x+1, checked_y+1))

                    if checked_x > 1 and enlarged_text[checked_y][checked_x-3] == regionIcon: newpoints.append((checked_x-3, checked_y))
                    else:
                        sidePoints.add((checked_x-1,checked_y))
                        sidePoints.add((checked_x-1,checked_y-1))
                        sidePoints.add((checked_x-1,checked_y+1))

                    if checked_x < len(enlarged_text[checked_y]) - 2 and enlarged_text[checked_y][checked_x+3] == regionIcon: newpoints.append((checked_x+3, checked_y))
                    else:
                        sidePoints.add((checked_x+1,checked_y))
                        sidePoints.add((checked_x+1,checked_y+1))
                        sidePoints.add((checked_x+1,checked_y-1))
                    
                    perimeter += 4 - len(newpoints)
                    for newpoint in newpoints:
                        if newpoint not in points and newpoint not in points_checked: points.append(newpoint)
                for point in points_checked: enlarged_text[point[1]][point[0]] = "."

                sidePoints = list(sidePoints)
                diagSearch = False
                border = []
                sides = -1
                for point in sidePoints:
                    if isVertice(point, sidePoints):
                        border.append(point)
                        break
                while len(sidePoints):
                    pointFound = False
                    for point in range(len(sidePoints)):
                        if (
                            border[-1][0] == sidePoints[point][0] and abs(border[-1][1] - sidePoints[point][1]) == 1 or
                            border[-1][1] == sidePoints[point][1] and abs(border[-1][0] - sidePoints[point][0]) == 1
                        ):
                            pointFound = True
                            diagSearch = False
                            border.append(sidePoints.pop(point))
                            break
                            
                    if not pointFound:
                        if not diagSearch:
                            diagSearch = True
                            border.append((border[-1][0] + border[-1][0] - border[-2][0], border[-1][1] + border[-1][1] - border[-2][1]))
                        else:
                            diagSearch = False
                            border.pop(-1)
                            for pointToCheck in range(len(sidePoints)):
                                if isSide(sidePoints[pointToCheck], sidePoints+border):
                                    border.append(sidePoints.pop(pointToCheck))
                                    break
                
                for point in border:
                    if isVertice(point, border): sides+=1

                result += sides*len(points_checked)

                if False:
                    for yD in range(len(enlarged_text_org)):
                        for xD in range(len(enlarged_text_org[yD])):
                            if (xD, yD) in border: print("#",end="")
                            else: print(enlarged_text_org[yD][xD],end="")
                        print()
                    input()

    return result

if __name__ == "__main__": print(main())