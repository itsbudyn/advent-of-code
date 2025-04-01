def draw(matrix,p1,p2):
    if (p1[0]!=p2[0] and p1[1]!=p2[1]): return

    line_h=[]
    line_v=[]
    line_h.append(p1[0])
    line_h.append(p2[0])
    line_v.append(p1[1])
    line_v.append(p2[1])
    line_h.sort()
    line_v.sort()

    for x in range(line_h[0],line_h[1]+1):
        for y in range(line_v[0],line_v[1]+1):
            matrix[y][x]+=1

points=[]
while True:
    try:
        points.append(list(input("Enter points A -> B: ").split(" -> ")))
    except KeyboardInterrupt:
        break

points_list=[]

for i in points[:]:
    for j in i:
        atob=[0,0]
        atob[0]=int(j.split(",")[0])
        atob[1]=int(j.split(",")[1])
        points_list.append( tuple(( atob[0],atob[1] )) )

del points

max_x=1
max_y=1
xs=[]
ys=[]

for i in points_list:
    xs.append(i[0])
    ys.append(i[1])

xs.sort()
ys.sort()

max_x+=xs[-1]
max_y+=ys[-1]

matrix=[[0 for x in range(max_x)] for y in range(max_y)]

print("\n\n")

for i in range(0,len(points_list),2):
    draw(matrix,points_list[i],points_list[i+1])

for i in matrix:
    for j in i:
        if j==0: print(".",end=" ")
        else: print(j,end=" ")
    print("")

overlaps=0
for i in matrix:
    for j in i:
        if j>1: overlaps+=1

print("Overlaps: ", overlaps)