import re

def main():
    with open("1.txt","r",encoding="UTF-8") as f: text = f.read()

    lines=text.split("\n")
    numbers=[]

    for i in lines:
        number=0
        for j in i:
            if re.match(r"[0-9]",j):
                number+=10*int(j)
                break
        for j in i[::-1]:
            if re.match(r"[0-9]",j):
                number+=int(j)
                break
        numbers.append(number)

    return sum(numbers)

if __name__ == "__main__": print(main())