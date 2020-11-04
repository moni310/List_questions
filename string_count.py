list=["aba","121","qoq","1221","464","non","opi"]
i=0
count=0
while i<len(list):
    j=0
    while j<len(list):
        if len(list)>1:
            if list[i][0]==list[i][-1]:
                count=count+1
            j=j+1
        i=i+1
print(count)