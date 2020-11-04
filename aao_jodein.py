element=[23,4,6,78,45,56,1,2,90,23,43]
i=0
odd_sum=0
even_sum=0
while i<len(element):
    if element[i]%2==0:
        even_sum=even_sum+element[i]
    else:
        odd_sum=odd_sum+element[i]
    i=i+1
print("sum of even number=",even_sum)
print("sum of odd number=",odd_sum)