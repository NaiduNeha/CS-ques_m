2. Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.


a=[int(i) for i in input().split()]

'''for i in l:
    if i  not in s:
        s.append(i)
'''
s=list(set(a))

print(s)
for i in s:
    if(a.count(i)>1):
        print(i)
        
        
        #OUTPUT:
        1 1 2 3 4 4 
[1, 2, 3, 4]
1
4
