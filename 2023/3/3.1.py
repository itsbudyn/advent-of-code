import re

def main():
    with open("3.txt","r",encoding="UTF-8") as f: text = f.read()
    lines = text.splitlines()

    part_numbers = []
    indexes_to_check = []

    for i in range(len(lines)):
        number = ""

        for j in range(len(lines[i])):
            if re.match(r"[0-9]",lines[i][j]):
                number += lines[i][j]
                if len(number) == 1: 
                    indexes_to_check.append((i-1,j-1))
                    indexes_to_check.append((i,j-1))
                    indexes_to_check.append((i+1,j-1))
                indexes_to_check.append((i-1,j))
                indexes_to_check.append((i+1,j))
            if len(number) > 0 and (not re.match(r"[0-9]",lines[i][j]) or j == len(lines[i])-1):
                indexes_to_check.append((i-1,j))
                indexes_to_check.append((i,j))
                indexes_to_check.append((i+1,j))

                for k in indexes_to_check:
                    if k[0] < 0 or k[0] > len(lines)-1 or k[1] < 0 or k[1] > len(lines[0])-1: continue
                    if not re.match(r"([0-9]|\.)",lines[k[0]][k[1]]):
                        part_numbers.append(int(number))
                        break
                number = ""
                indexes_to_check = []

    return sum(part_numbers)

if __name__ == "__main__": print(main())