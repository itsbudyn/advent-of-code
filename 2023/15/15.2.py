def lensToStr(lens:list):
    return f"{lens[0]} {lens[1]}"

def lensAdd(boxes:list, lens:list):
    # replace lens
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if lens[0] in boxes[i][j]:
                boxes[i][j] = lensToStr(lens)
                return boxes

    # add lens
    if len(boxes) > 1:
        maxFocals = []
        for i in boxes:
            maxFocal = 0
            for j in i:
                if int(j[-1]) > maxFocal: maxFocal = int(j[-1])
            maxFocals.append(maxFocal)

        for i in range(len(maxFocals)-1):
            if int(lens[1]) < maxFocals[i+1]:
                boxes[i].append(lensToStr(lens))
                return boxes
    
    boxes.append([lensToStr(lens)])
    return boxes

def lensRemove(boxes:list, lensLabel:str):
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if lensLabel in boxes[i][j]:
                boxes[i].pop(j)
                return boxes
    return boxes

def main():
    with open("2023/15/15.txt","r",encoding="UTF-8") as f: text = f.read().split(",")

    boxes = []

    for i in text:
        print(i)
        if "=" in i:
            lens = i.split("=")
            boxes = lensAdd(boxes,lens)
        elif "-" in i:
            lensLabel = i[:-1]
            boxes = lensRemove(boxes,lensLabel)
        print(boxes)

if __name__ == "__main__": print(main())