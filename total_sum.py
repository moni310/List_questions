num=30
n=[10,11,12,13,14,17,18,19]
i=0
while i<len(n):
    j=-1
    while j<len(n):
        if n[i]+n[j]==30:
            k=[n[i],n[j]]
            print(k)
            j=j-1
        i=i+1
# n=[10,11,12,13,14,17,18,19]
# i=0
# while i<len(n):
#     j=1
#     while j<len(n):
#         if n[j]+n[j]==30:
#             k=[n[i],n[j]]
#             j=j+1
#         i=i+1
# print(k)
