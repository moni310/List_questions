list=[1,-4,7,5,3,-9,-4,8,2,-3,9]
i=0
count=0
count1=0
while i<len(list):
    if list[i]>=0:
       count=count+1
    else:
       count1=count1+1
    i=i+1
print("positive num",count)
print("negative num",count1)