def getMovement(sequence:str, keymap:dict, startpos:tuple, isKp1:bool):
    keypos = startpos
    result = ""
    for btn in sequence:
        revMoves = False
        movement = (keypos[0] - keymap[btn][0], keypos[1] - keymap[btn][1])
        if keymap[" "] == (keypos[0] - movement[0], keypos[1]): revMoves = True
        newMoves = ""
        newMoves += "<"*movement[0] if movement[0] > 0 else ">"*abs(movement[0])
        newMoves += "^"*movement[1] if movement[1] > 0 else "v"*abs(movement[1])
        if revMoves: newMoves = newMoves[::-1]
        newMoves += "A"
        result += newMoves
        keypos = (keypos[0] - movement[0], keypos[1] - movement[1])
    return result

def main():
    with open("2024/21/21.txt","r",encoding="UTF-8") as f: codes = f.read().split("\n")

    kp1 = (
        ("7", "8", "9"),
        ("4", "5", "6"),
        ("1", "2", "3"),
        (" ", "0", "A")
    )
    kp2 = (
        (" ", "^", "A"),
        ("<", "v", ">")
    )

    kp1Start = (2, 3)
    kp2Start = (2, 0)
    kp1Map = {}
    kp2Map = {}

    for y in range(len(kp1)):
        for x in range(len(kp1[y])): kp1Map[kp1[y][x]] = (x, y)
    for y in range(len(kp2)):
        for x in range(len(kp2[y])): kp2Map[kp2[y][x]] = (x, y)

    result = 0
    for code in codes:
        kp1Presses = getMovement(code, kp1Map, kp1Start, True)
        kp2Presses = getMovement(kp1Presses, kp2Map, kp2Start, False)
        kp3Presses = getMovement(kp2Presses, kp2Map, kp2Start, False)
        print(len(kp3Presses), int(code[:-1]))
        result += len(kp3Presses) * int(code[:-1])
    
    return result

if __name__ == "__main__": print(main())

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
#
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+