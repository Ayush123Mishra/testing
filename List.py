a=[]
n=int(input("how many Students"))
while(n>=1):
    marks=int(input("Enter Marks"))
    a.append(marks)
    n=n-1
x=int(input("Enter No. to be Search"))
if x in a:
    print("Found ",x)
else:
    print("Not Found ",x)
