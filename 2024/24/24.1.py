def main():
    with open("24.txt","r",encoding="UTF-8") as f: text = f.read().split("\n\n")

    wires = {}
    lut = {
        "OR":"|",
        "XOR":"^",
        "AND":"&"
    }
    text[1] = text[1].split("\n")

    for i in text[0].split("\n"):
        wire = i.split(": ")
        wires[wire[0]] = wire[1]

    while text[1]:
        indexesToRemove = []
        for i in range(len(text[1])):
            eq = text[1][i]
            eq = eq.split(" ")
            solved = False
            if eq[0] in wires.keys() and eq[2] in wires.keys() and eq[4] not in wires.keys(): 
                wires[eq[4]] = str(eval(f"{wires[eq[0]]} {lut[eq[1]]} {wires[eq[2]]}"))
                solved = True
            if eq[0] in wires.keys() and eq[2] not in wires.keys() and eq[4] in wires.keys():
                wires[eq[2]] = str(eval(f"{wires[eq[0]]} {lut[eq[1]]} {wires[eq[4]]}"))
                solved = True
            if eq[0] not in wires.keys() and eq[2] in wires.keys() and eq[4] in wires.keys():
                wires[eq[0]] = str(eval(f"{wires[eq[2]]} {lut[eq[1]]} {wires[eq[4]]}"))
                solved = True
            if solved: indexesToRemove.append(i)
        while indexesToRemove: text[1].pop(indexesToRemove.pop(-1))

    out = ""
    for i in sorted(wires.keys()):
        if "z" in i: out+=wires[i]
    out += "b0"
    return eval(out[::-1])

if __name__ == "__main__": print(main())
