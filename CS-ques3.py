3. Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number.


n=int(input("enter value to get pairs:"))
l=[int(i) for i in input().split()]
l.sort()
m=[]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        s=[]
        if(i!=j):
            if(l[i]+l[j]==n):
                s.append(l[i])
                s.append(l[j])
                m.append(s)
print(m)
for i in range(0,len(m)//2):
    print(m[i])
    
    
    #OUTPUT:
    enter value to get pairs:6
2 4 1 3 5
[[1, 5], [2, 4], [4, 2], [5, 1]]
[1, 5]
[2, 4]
