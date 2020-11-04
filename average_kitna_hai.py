a=[33,56,34,2,3,5,4]
i=0
even_count=0
even_sum=0
odd_count=0
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
print("average of sum=",even_average)
print("average of odd=",odd_average)