def basinSearch(arr,x,y):
    points_to_check=[[x,y]]
    basin=[]
    arr_x=len(arr[0])
    arr_y=len(arr)
    

heatmap=[]

while True:
    try:
        x=input("Enter map: ")
        heatmap.append([int(i) for i in str(x)])
    except KeyboardInterrupt:
        break
print("\n\n")
for i in heatmap:
    print(i)

x=len(heatmap[0])
y=len(heatmap)

lowpoints=[]
for i in range(y):
    for j in range(x):
        score=0
        if j-1 in range(x):
            if heatmap[i][j-1]>heatmap[i][j]: score+=1
        else: score+=1
        if j+1 in range(x):
            if heatmap[i][j+1]>heatmap[i][j]: score+=1
        else: score+=1
        if i-1 in range(y):
            if heatmap[i-1][j]>heatmap[i][j]: score+=1
        else: score+=1
        if i+1 in range(y):
            if heatmap[i+1][j]>heatmap[i][j]: score+=1
        else: score+=1
        if score==4: lowpoints.append(heatmap[i][j])
            
for i in range(len(lowpoints)):
    lowpoints[i]+=1

print(sum(lowpoints))