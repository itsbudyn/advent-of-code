def main():
    with open("9.txt","r",encoding="UTF-8") as f: text = f.read()
    diskmap, filesize = [], []
    checksum = 0

    for i in range(len(text)):
        if i%2: diskmap+=["."]*int(text[i])
        else: 
            diskmap+=[f"{i//2}"]*int(text[i])
            filesize.append(int(text[i]))

    for i in range(len(filesize)-1, 0, -1):
        while diskmap[-1] == ".": del diskmap[-1]
        holeBegin, holeEnd = 0, 0

        for blockRev in range(len(diskmap)-1, -1, -1):
            if diskmap[blockRev] == str(i):
                movedFileEnd = blockRev
                break

        for block in range(len(diskmap)):
            if not holeBegin and diskmap[block] == ".": holeBegin = block
            elif holeBegin and diskmap[block] != ".": holeEnd = block

            if holeBegin and holeEnd:
                if holeEnd - holeBegin >= filesize[i]:
                    for blockMoved in range(filesize[i]):
                        diskmap[holeBegin + blockMoved] = diskmap[movedFileEnd - blockMoved]
                        diskmap[movedFileEnd - blockMoved] = "."
                    break
                else: holeBegin, holeEnd = 0, 0

            if block >= movedFileEnd - filesize[i] + 1: break
        
    for i in range(len(diskmap)): 
        if diskmap[i] != ".": checksum += i*int(diskmap[i])
    return checksum

if __name__ == "__main__": print(main())