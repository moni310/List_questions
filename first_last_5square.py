i=0
empty_list=[ ]
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
while i<len(list):
    if list[i]<list[5]:
        square=list[i]*list[i]
        empty_list.append(square)
    i=i+1
k=empty_list
j=0
empty=[ ]
while j<len(list):
    if list[-j]>list[-6]:
        square1=list[-j]*list[-j]
        empty.append(square1)
    j=j+1
print(k)
print(empty)