data = [60, 82, 53, 81]
data.sort()

upper = len(data)
mid =  int(upper/ 2)

data2 = data[mid-1:upper-1]
data2.sort(reverse = True)

for i in range(mid-1):
    print(data[i], end=" ")
print(data[upper-1], end=" ")

for j in range(mid):
    print(data2[j], end=" ")

print("Done")