def isUnsorted(i:list, sortmap:dict):
    for j in range(1,len(i)):
        if i[j] not in sortmap.keys(): continue
        arr_to_check, values = i[:j], sortmap[i[j]]

        for k in values:
            if k in arr_to_check: return True
    return False

def main():
    with open("5.txt","r",encoding="UTF-8") as f: text = f.read().split("\n\n")

    result = 0
    badpages = []
    text[0], text[1] = text[0].split("\n"), text[1].split("\n")
    sortmap = {}
    
    for i in range(len(text[1])): text[1][i] = list(map(int, text[1][i].split(",")))

    for i in text[0]:
        arr = list(map(int,i.split("|")))
        if arr[0] in sortmap.keys(): sortmap[arr[0]].append(arr[1])
        else: sortmap[arr[0]] = [arr[1]]

    for i in text[1]: 
        if isUnsorted(i,sortmap): badpages.append(i)

    for i in range(len(badpages)):
        while isUnsorted(badpages[i], sortmap):
            for j in range(1,len(badpages[i])):
                for k in range(len(badpages[i][:j])):
                    if badpages[i][j] in list(sortmap.keys()) and badpages[i][k] in sortmap[badpages[i][j]]: badpages[i].insert(k, badpages[i].pop(j))

    for i in badpages: result+=i[len(i)//2]

    return result

if __name__ == "__main__": print(main())