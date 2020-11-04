a=[6,8,71,22,34,12,33,81,45]
i=0
odd_count=0
even_count=0
even_sum=0
odd_sum=0
even_average=0
odd_average=0
while i<len(a):
    if a[i]%2==0:
        even_count=even_count+1
        even_sum=even_sum+a[i]
        even_average=even_sum//even_count
    else:
        odd_count=odd_count+1
        odd_sum=odd_sum+a[i]
        odd_average=odd_sum//odd_count
    i=i+1
print("number of odd=",odd_count)
print("number of even=",even_count)
print("sum of even number=",even_sum)
print("average of even=",even_average)
print("sum of odd number=",odd_sum)
print("average of odd=",odd_average)
print("total sum=",even_sum+odd_sum)
print("total number=",odd_count+even_count)
print("total_average=",even_average+odd_average)