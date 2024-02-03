lanternfish=[int(i) for i in list(input("Enter lanternfish states: ").split(","))]

days=80

for i in range(days):
    for j in range(len(lanternfish)):
        if lanternfish[j]!=0: lanternfish[j]-=1
        else: 
            lanternfish[j]=6
            lanternfish.append(8)

print(len(lanternfish))