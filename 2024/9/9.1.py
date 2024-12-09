def main():
    with open("9.txt","r",encoding="UTF-8") as f: text = f.read()
    diskmap = []
    checksum = 0

    for i in range(len(text)):
        if i%2: diskmap+=["."]*int(text[i])
        else: diskmap+=[f"{i//2}"]*int(text[i])

    usedSpace = len(diskmap) - diskmap.count(".")
    resume = 0

    while len(diskmap) != usedSpace:
        for block in range(resume, len(diskmap)):
            if diskmap[block]==".":
                resume = block
                for blockRev in range(len(diskmap)-1,-1,-1):
                    if diskmap[blockRev] != ".":
                        blockToPlace = diskmap[blockRev]
                        diskmap[blockRev] = "."
                        break
                diskmap[block] = blockToPlace
                diskmap[-1] = "."
                while diskmap[-1] == ".": del diskmap[-1]
                break

    for i in range(len(diskmap)): checksum+=i*int(diskmap[i])
    return checksum

if __name__ == "__main__": print(main())