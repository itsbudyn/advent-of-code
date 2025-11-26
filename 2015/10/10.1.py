with open("10.txt", "r", encoding="UTF-8") as f: text: list[str] = list(f.read())

def lookAndSay(number: list[str]) -> list[str]:
    number.append(" ")
    output: str = ""

    digit: str = number[0]
    reps: int = 0

    for currentDigit in number:
        if currentDigit != digit:
            output += f"{reps}{digit}"
            reps = 0
            digit = currentDigit
        reps += 1

    return list(output)

def main() -> tuple[int, ...]:
    out: list[int] = []
    number: list[str] = text
    for i in range(50):
        number = lookAndSay(number)
        if i in [39, 49]: out.append(len(number))
    return tuple(out)

if __name__ == "__main__": print(main())