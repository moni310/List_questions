num=int(input("enter the number"))
num1=int(input("enter the number"))
i=1
m=1
while i<num or i<num1:
    if  num%i==0 or num1%i==0:

        i=i+1
        print(m*i)
