import re

def main():
    with open("3.txt","r",encoding="UTF-8") as f: text = f.read()

    result = 0
    muls = re.findall(r"mul\([0-9]+,[0-9]+\)",text)
    for i in muls:
        factors = i[4:-1].split(",")
        factors = list(map(int, factors))
        result += factors[0] * factors[1]

    return result

if __name__ == "__main__": print(main())