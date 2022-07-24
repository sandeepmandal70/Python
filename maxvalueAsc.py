listy = list()
temp = list()

n = int(input())
for i in range(n):listy.append(int(input()))
max = 0

for i in range(n):
    if(i==0):
        temp.append(listy[i])
    else:
        if(listy[i]>listy[i-1]):
            temp.append(listy[i])
            print()
        else:
            temp.clear()
            temp.append(listy[i])
    if(sum(temp)>max):
        max = sum(temp)
print(max)    

 


# print("res",max)