import re

def main():
    with open("1.txt","r",encoding="UTF-8") as f: text = f.read()

    digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    lines=text.split("\n")
    numbers=[]

    for i in lines:
        tens, ones=0, 0
        buffer=""
        for j in i:
            if re.match(r"[0-9]",j):
                tens=int(j)
            else:
                buffer+=j
                for k in digits.keys():
                    if k in buffer:
                        tens=digits[k]
                        break
            if tens: break

        buffer=""
        for j in i[::-1]:
            if re.match(r"[0-9]",j):
                ones+=int(j)
                break
            else:
                buffer+=j
                for k in digits.keys():
                    if k in buffer[::-1]:
                        ones+=digits[k]
                        break
            if ones: break
                    
        numbers.append(10*tens+ones)

    return sum(numbers)

if __name__ == "__main__": print(main())