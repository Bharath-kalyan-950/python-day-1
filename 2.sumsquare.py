def sumsquare(a):
    odd=0
    even=0
    for i in a:
        if(i%2==0):
            even=even+i**2
        else:
            odd=odd+i**2
    l=[even,odd]
    return l

n=int(input("enter no. of terms"))
l=[]
for j in range(0,n):
    m=int(input("enter a no. :"))
    l.append(m)

print(sumsquare(l))
