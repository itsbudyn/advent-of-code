from re import findall

def main() -> None:
    def getSum(text: list[str]) -> int: return sum(map(int, findall(r"[-]*[0-9]+", "".join(text))))
    with open("2015/12/12.txt", "r", encoding="UTF-8") as f: text: list[str] = list(f.read())
    print("PART 1:", getSum(text))

    openingCBrackets: list[int] = []
    ignoredOpeningBrackets: int = 0
    redDetected: bool = False

    for index in range(len(text)):
        match text[index]:
            case "{": 
                if not redDetected: openingCBrackets.append(index)
                else: ignoredOpeningBrackets += 1
            case "}": 
                if ignoredOpeningBrackets > 0: ignoredOpeningBrackets -= 1
                elif redDetected: 
                    for wipeIndex in range(openingCBrackets.pop(-1), index + 1): text[wipeIndex] = " "
                    redDetected = False
                else: openingCBrackets.pop(-1)

        if openingCBrackets and index <= len(text) - 5 and "".join([text[index], text[index + 1], text[index + 2], text[index + 3], text[index + 4]]) == "\"red\"": redDetected = True
    
    print("".join(text))
    print(getSum(text))

if __name__ == "__main__": print(main())