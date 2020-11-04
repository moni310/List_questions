a=[[8,3,4],[1,5,9],[6,7,2]]
rows=0
coloum=0
left_digonal=0
right_digonal=0
i=0
while i<len(a):
    j=0
    while j<len(a):
        rows=rows+a[i][j]
        coloum=coloum+a[j][i]
        j=j+1
    left_digonal=left_digonal+a[i][len(a)-(i+1)]
    right_digonal=right_digonal+a[i][i]
    i=i+1
print("rows",rows,"=","coloum",coloum)
print("left_digonal",left_digonal,"=","right_digonal",right_digonal)
print("this is magic square")