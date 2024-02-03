def series(x):
    out=0
    for i in range(x):
        out+=i+1
    return out

positions=[int(i) for i in list(input("Enter positions: ").split(","))]

positions.sort()

diffs=[]
for i in range(positions[0],positions[-1]+1):
    diff=["pos","cost"]
    costs=[]
    diff[0]=i

    for j in positions:
        costs.append(series(abs(i-j)))

    diff[1]=sum(costs)
    diffs.append(diff)

costs=[]

for i in diffs:
    print(i)
    costs.append(i[1])

costs.sort()
print("Cheapest route will use",costs[0],"of fuel")