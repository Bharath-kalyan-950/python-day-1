a=int(input("enter the number of loaves:"))
c=int(input("enter the number of day old loaves"))
b=a*185
print("loaves discount",b)
d=(c*185)-(c*185*.6)
print("regular price",d)
print("total amount",b+d)
