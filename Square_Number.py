n=int(input())
for i in range(2,n):
    if i*i==n:
        print("True")
        break
else:
    print("False")