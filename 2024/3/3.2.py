import re

def main():
    with open("3.txt","r",encoding="UTF-8") as f: text = f.read()

    result = 0
    enabled = True
    muls = re.findall(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))",text)

    for i in range(len(muls)):
        if muls[i][0] and enabled:
            factors = muls[i][0][4:-1].split(",")
            factors = list(map(int, factors))
            result += factors[0] * factors[1]
        elif muls[i][1]: enabled = True
        elif muls[i][2]: enabled = False

    return result

if __name__ == "__main__": print(main())