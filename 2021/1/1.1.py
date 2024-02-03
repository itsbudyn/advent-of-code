measurements=[]
while True:
    try:
        measurements.append(int(input("Enter a measurement: ")))
    except ValueError:
        break

gts=0
for i in range(len(measurements)-1):
    if measurements[i] < measurements[i+1]:
        gts+=1

print(gts)