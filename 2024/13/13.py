import re

def main(part:int):
    with open("2024/13/13.txt","r",encoding="UTF-8") as f: text = f.read().split("\n\n")
    result = 0

    for equation in text: 
        numbers = re.findall(r"[XY][\+=][0-9]+",equation)
        for number in range(len(numbers)): numbers[number] = int(numbers[number][2:])

        if part == 2: 
            numbers[4] += 10000000000000
            numbers[5] += 10000000000000

        equationMatrix = [
            [numbers[0], numbers[2], numbers[4]],
            [numbers[1], numbers[3], numbers[5]] 
        ]
        
        cf1, cf2 = equationMatrix[0][0], equationMatrix[1][0]
        equationMatrix[0] = [num * cf2 for num in equationMatrix[0]]
        equationMatrix[1] = [num * cf1 for num in equationMatrix[1]]

        equationMatrix[1][1] -= equationMatrix[0][1]
        equationMatrix[1][2] -= equationMatrix[0][2]

        b = equationMatrix[1][2] / equationMatrix[1][1]
        if b % 1: continue
        a = (equationMatrix[0][2] - equationMatrix[0][1]*b) / equationMatrix[0][0]
        if a % 1: continue

        result += int(a*3 + b)

    return result

if __name__ == "__main__": 
    print("Part 1:", main(1))
    print("Part 2:", main(2))