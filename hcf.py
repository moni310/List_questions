num=int(input("enter the number"))
num1=int(input("enter the number"))
i=1
while i<num and i<num1:
    if num%i==0 and num1%i==0:
        hcf=i
    i=i+1
print(hcf)