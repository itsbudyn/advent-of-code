def getBadStep(arr: list):
    minDiff = 1
    maxDiff = 3

    incline = arr[0] - arr[1] < 0

    for j in range(len(arr)-1):
        slant = arr[j] - arr[j+1]
        if abs(slant) > maxDiff or abs(slant) < minDiff or (slant < 0) != incline: return j
    return -1


def main():
    with open("2.txt","r",encoding="UTF-8") as f: text = f.readlines()

    safe = 0

    for i in text:
        arr = i.split(" ")
        arr = list(map(int, arr))

        badStep = getBadStep(arr)
        match badStep:
            case -1: safe+=1
            case _:
                arr1, arr2, arr3 = arr.copy(), arr.copy(), arr.copy()
                del arr1[badStep], arr2[badStep-1], arr3[badStep+1]

                if getBadStep(arr1) == -1 or getBadStep(arr2) == -1 or getBadStep(arr3) == -1: safe+=1
         
    return safe

if __name__ == "__main__": print(main())