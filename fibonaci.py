t = int(input("Enter a Number : "))
start = 0
next = 1
for i in range(t):
    print(start)
    temp = start + next
    start = next
    next = temp
