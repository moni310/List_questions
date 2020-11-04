a=[3,7,5,3,0,8,56,5,67,4,91]
maxi=0
i=0
while i<len(a):
    if a[i]>maxi:
        maxi=a[i]
    i=i+1
    b=0
    j=0
    while j<len(a):
        if maxi>a[j] and b<a[j]:
            b=a[j]
        j=j+1
print(b)
