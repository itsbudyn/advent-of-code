def main():
    with open("2.txt","r",encoding="UTF-8") as f: text = f.readlines()

    safe    = 0
    minDiff = 1
    maxDiff = 3

    for i in text:
        arr = i.split(" ")
        arr = list(map(int, arr))

        incline = arr[0] - arr[1] < 0

        unsafe = False
        for j in range(len(arr)-1):
            slant = arr[j] - arr[j+1]
            if abs(slant) > maxDiff or abs(slant) < minDiff or (slant < 0) != incline:
                unsafe = True
                break

        if not unsafe: safe += 1
         
    return safe

if __name__ == "__main__": print(main())