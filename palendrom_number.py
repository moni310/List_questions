n=[2,5,6,10,6,9,20,121,18]
i=len(n)
list=[ ]
while i>0:
    i=i-1
    a=n[i]
    list.append(a)
print(list)
if n==list:
    print("it is palindrom number")
else:
    print("it is not palindrom number")
