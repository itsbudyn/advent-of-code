import re

def main():
    with open("6.txt","r",encoding="UTF-8") as f: text=f.readlines()

    for i in range(len(text)): text[i] = int("".join(re.findall(r"[0-9]+",text[i])))

    possibilities = 0

    time = text[0]
    distance = text[1]
    speed = 1
    while speed < time:
        if speed * (time - speed) > distance: possibilities += 1
        speed += 1

    return possibilities

if __name__ == "__main__": print(main())