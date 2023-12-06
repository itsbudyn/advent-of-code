import re

def main():
    with open("6.txt","r",encoding="UTF-8") as f: text=f.readlines()

    for i in range(len(text)):
        text[i] = re.findall(r"[0-9]+",text[i])
        for j in range(len(text[i])): text[i][j] = int(text[i][j])

    all_possibilities = []

    for i in range(len(text[0])):
        possibilities = 0

        time = text[0][i]
        distance = text[1][i]

        speed = 1
        while speed < time:
            if speed * (time - speed) > distance: possibilities += 1
            speed += 1
        all_possibilities.append(possibilities)

    multiples = 1
    for i in all_possibilities: multiples*=i

    return multiples

if __name__ == "__main__": print(main())