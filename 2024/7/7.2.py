def isPossible(result:int, numbers:list):
    while len(numbers) > 1:
        resultStr, numberStr, possibleNewResult = str(result), str(numbers[-1]), False
        if result > 0 and len(resultStr) > len(numberStr) and resultStr[-len(numberStr):] == numberStr: possibleNewResult = int(resultStr[:-len(numberStr)])

        if possibleNewResult and isPossible(possibleNewResult, numbers[:-1]): result = possibleNewResult 
        elif result % numbers[-1] or isPossible(result-numbers[-1], numbers[:-1]): result-=numbers[-1]
        else: result//=numbers[-1]
        numbers.pop(-1)
    return result == numbers[0]

def main():
    with open("7.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    result = 0

    for i in range(len(text)): text[i] = text[i].split(": ")
    for i in range(len(text)): 
        text[i][0], text[i][1] = int(text[i][0]), list(map(int, text[i][1].split(" ")))

    for i in text:
        if isPossible(i[0],i[1]): result+=i[0]
    return result

if __name__ == "__main__": print(main())