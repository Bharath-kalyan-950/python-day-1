number=int(input("enter a num :"))
def isahappynumber(number):
    reminder=0
    sum=0
    while(number!=0):
        reminder=number%10
        sum=sum+(reminder*reminder);
        number=number//10
        return sum

result=number
while (result!=1 and result!=4):
    result=isahappynumber(result)
if(result==1):
    print("ahappynumber")
elif(result==4):
    print("isnotahappynumber")
