def stair(n):
    for i in range(0,n+1):
        num=""
        for j in range(0,i+1):
            num+=str(j)
        print(num)

def pi(n):
    sharp=""
    for i in range(0,n+1):
        sharp=sharp +"#"
        print(sharp)
    while(n>0):
        print(sharp[0:n])
        n-=1

x= int(input("Please enter an integer"))

for i in range(0,x):
    pi(i)
