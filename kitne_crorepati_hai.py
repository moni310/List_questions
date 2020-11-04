list=[3000,600000,324990909,909909000,30000,5600000,690909090,31010101,532010,510,4100]
i=0
count=0
count1=0
count2=0
while i<len(list):
    if list[i]>=10000000:
        count=count+1
    elif list[i]>=100000:
        count1=count1+1
    else:
        count2=count2+1
    i=i+1
print(count,"carorpati")
print(count1,"lakhpati")
print(count2,"dilwale")