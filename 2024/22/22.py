def mix(secret:int, number:int): return secret ^ number
def prune(secret:int): return secret % 16777216
def evolve(secret:int):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

def main():
    with open("2024/22/22.txt","r",encoding="UTF-8") as f: secrets = list(map(int, f.read().split("\n")))
    result = 0
    monkeys = {}
    sequenceToPriceMap = {}

    for i in range(len(secrets)): monkeys[i] = {"secret":secrets[i], "prices":[secrets[i] % 10], "changes": [], "sequences": set()}

    for i in range(2000):
        for j in monkeys.keys():
            monkeys[j]["secret"] = evolve(monkeys[j]["secret"])
            monkeys[j]["prices"].append(monkeys[j]["secret"] % 10)
            monkeys[j]["changes"].append(monkeys[j]["prices"][-1] - monkeys[j]["prices"][-2])
            if i > 4:
                seq = (monkeys[j]["changes"][i-4], monkeys[j]["changes"][i-3], monkeys[j]["changes"][i-2], monkeys[j]["changes"][i-1])
                if seq not in monkeys[j]["sequences"]:
                    if seq not in sequenceToPriceMap.keys(): sequenceToPriceMap[seq] = [monkeys[j]["prices"][i]]
                    else: sequenceToPriceMap[seq].append(monkeys[j]["prices"][i])
                    monkeys[j]["sequences"].add(seq)

    sums = set()
    for i in monkeys.keys(): result += monkeys[i]["secret"]
    for i in sequenceToPriceMap.values(): sums.add(sum(i))

    return f"Part 1: {result}\nPart 2: {max(sums)}"

if __name__ == "__main__": print(main())