sums=[]
measurements=[]

while True:
    try:
        measurements.append(int(input("Enter a measurement: ")))
    except ValueError:
        break

for i in range(len(measurements)-2):
   sums.append(measurements[i]+measurements[i+1]+measurements[i+2])

gts=0
for i in range(len(sums)-1):
    if sums[i] < sums[i+1]:
        gts+=1

print(gts)