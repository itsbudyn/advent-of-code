from copy import deepcopy

def solve(puzzle:list):
    maxSteps = len(puzzle) ** 2
    bearing = 0
    nextpos = []
    steps = []
    for y in range(len(puzzle)):
        if len(nextpos): break
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == "^": 
                nextpos = (x, y-1)
                break
    if not len(nextpos): return None
    steps.append(nextpos)
    steps.append(nextpos)

    while True:
        for i in nextpos:
            if i >= len(puzzle) or 0 > i: return steps

        if puzzle[nextpos[1]][nextpos[0]] == "#":
            bearing = (bearing + 90) % 360
            steps.pop(-1)
            nextpos = steps[-1]
            puzzle[nextpos[1]][nextpos[0]] = "+"

        match bearing:
            case   0: nextpos = (nextpos[0],nextpos[1]-1)
            case  90: nextpos = (nextpos[0]+1,nextpos[1])
            case 180: nextpos = (nextpos[0],nextpos[1]+1)
            case 270: nextpos = (nextpos[0]-1,nextpos[1])

        steps.append(nextpos)
        if len(steps) > maxSteps: return False

def getNextStep(step:tuple, bearing:int):
    match bearing:
        case 0:     step = (step[0],step[1]-1)
        case 90:    step = (step[0]+1,step[1])
        case 180:   step = (step[0],step[1]+1)
        case 270:   step = (step[0]-1,step[1])
    return step

def main():
    with open("6.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    bearing = 0
    possibleObstructions = set()
    
    text = list(map(list, text))

    orgSteps = solve(deepcopy(text))

    for step in range(len(orgSteps)):
        nextstep = orgSteps[step]
        
        if nextstep[0] >= len(text) or nextstep[0] < 0 or nextstep[1] >= len(text) or nextstep[1] < 0: continue
        
        while text[nextstep[1]][nextstep[0]] == "#": 
            bearing = (bearing + 90) % 360
            nextstep = getNextStep(nextstep, bearing)
        text_to_try = deepcopy(text)
        text_to_try[nextstep[1]][nextstep[0]] = "#"
        if solve(text_to_try) == False: possibleObstructions.add((nextstep[0],nextstep[1]))

    return len(possibleObstructions)
            
if __name__ == "__main__": print(main())