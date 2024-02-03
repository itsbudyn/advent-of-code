usr=str(input("Enter lanternfish states: "))
lanternfish=[usr.count(str(i)) for i in range(0,9)]

for day in range(256):
    lanternfish[(day+7)%9]+=lanternfish[day%9]

print(sum(lanternfish))    