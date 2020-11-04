element=[34,5,7,8,9,1,2,3,4,55,78]
i=0
odd_count=0
even_count=0
while i<len(element):
    if element[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i=i+1
print("even number=",even_count)
print("odd number=",odd_count)