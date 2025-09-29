print("right triangle pattern")
print("-------------------------")
n=int(input("Enter the number"))
for i in range(1, n+1):
    for space in range(n - i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
        print()
