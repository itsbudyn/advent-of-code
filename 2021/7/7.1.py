positions=[int(i) for i in list(input("Enter positions: ").split(","))]

diffs=[]
for i in positions:
    diff=["pos","cost"]
    costs=[]
    diff[0]=i

    skip=False
    for j in diffs:
        if i==j[0]:
            skip=True
            break

    if skip: continue
    for j in positions:
        costs.append(abs(i-j))

    diff[1]=sum(costs)
    diffs.append(diff)

costs=[]

for i in diffs:
    print(i)
    costs.append(i[1])

costs.sort()
print("Cheapest route will use",costs[0],"of fuel")

