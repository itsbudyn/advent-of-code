def predictNextNumber(arr:list):
    arr = getDiffArray(arr)
    for i in range(len(arr)-1,0,-1): arr[i-1].append(arr[i-1][-1]+arr[i][-1])
    return arr[0][-1]

def getDiffArray(arr:list):
    arr = [arr]

    while True:
        diffs = []
        for i in range(len(arr[-1])-1): diffs.append(arr[-1][i+1] - arr[-1][i])
        arr.append(diffs)
        if arr[-1][0] == 0 and sorted(arr[-1])[0] == sorted(arr[-1])[-1]: break 

    return arr

def main():
    with open("9.txt","r",encoding="UTF-8") as f: text = f.read().splitlines()

    for i in range(len(text)):
        text[i] = text[i].split(" ")
        for j in range(len(text[i])): text[i][j] = int(text[i][j])

    predicted = []
    for i in text: predicted.append(predictNextNumber(i))

    return sum(predicted)

if __name__ == "__main__": print(main())