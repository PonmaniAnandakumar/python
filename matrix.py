A =[[1,2,3],[5,3,1],[7,9,8]]
B = [[3,4],[12,4],[8,14]]
p=len(A)
q=len(A[0])
t=len(B)
r=len(B[0])

if(q!=t):
    print("error! matrix sizes are not compatible")
    quit()


c=[]
for row in range(p):
    curr_row=[]
    for col in range(r):
        curr_row.append(0)
    c.append(curr_row)

for i in range(p):
    for j in range(r):
        curr_val=0
        for k in range(q):
            curr_val+=A[i][k]*B[k][j]
        c[i][j]=curr_val
    
print(c)
