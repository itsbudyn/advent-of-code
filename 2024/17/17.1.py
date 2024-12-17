def main():
    with open("2024/17/17.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    registers = []
    program = []
    for i in text: registers.append(i.split(" ")[-1])
    program = registers.pop(-1).split(",")

    registers = list(map(int, registers[:-1]))
    program = list(map(int, program))
    out = ""
    pc = 0
    while True:
        opc = program[pc]
        opr = program[pc+1]
        match opr:
            case 0: c_opr = 0
            case 1: c_opr = 1
            case 2: c_opr = 2
            case 3: c_opr = 3
            case 4: c_opr = registers[0]
            case 5: c_opr = registers[1]
            case 6: c_opr = registers[2]
        match opc:
            case 0: registers[0] = registers[0] // 2**c_opr
            case 1: registers[1] = registers[1] ^ opr
            case 2: registers[1] = c_opr % 8
            case 3:
                if registers[0] != 0:
                    pc = opr
                    continue
            case 4: registers[1] = registers[1] ^ registers[2]
            case 5: out += str(c_opr % 8) + ","
            case 6: registers[1] = registers[0] // 2**c_opr
            case 7: registers[2] = registers[0] // 2**c_opr
        pc += 2
        if pc >= len(program)-1: break
            
    return out[:-1]

if __name__ == "__main__": print(main())