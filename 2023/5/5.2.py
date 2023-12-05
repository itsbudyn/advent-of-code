def origin(used_map: list, obj: int):
    for i in used_map:
        if obj < i[0] + i[2] and obj >= i[0]: return i[1] + obj - i[0]
    return obj

def main():
    with open("2023/5/5.txt","r",encoding="UTF-8") as f: text = f.readlines()

    seed_pairs = [int(i) for i in text[0][7:-1].split(" ")]

    ranges = []
    for i in range(0,len(seed_pairs),2): ranges.append([seed_pairs[i],seed_pairs[i]+seed_pairs[i+1]])
    ranges = sorted(ranges)

    map_arr = []
    for i in text[2:]:
        if "map" in i: map_arr.append([])
        elif i != "\n": map_arr[-1].append([int(j) for j in i.split(" ")])

    i = 1
    while True:
        seedCandidate = i
        for j in map_arr[::-1]: seedCandidate = origin(j,seedCandidate)
        
        for j in ranges:
            if seedCandidate >= j[0] and seedCandidate <= j[1]: return i

        i+=1

if __name__ == "__main__": print(main())