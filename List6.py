n=int(input("How Many Elements in List"))
a=[]
i=0
while(i<n):
    x=int(input("Enter Element for the List"))
    a.append(x)
    i=i+1
print(a)
i=n-1
while(i>=0):
    print(a[i])
    i=i-1
    


