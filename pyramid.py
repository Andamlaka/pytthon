rows=5
row=1
while row<=rows:
    spaces=rows-row
    while spaces > 0:
        print(" ", end=" ")
        spaces = spaces -1

    col=1
    while col <= (2 * row -1):
        print("*", end=" ")
        col=col+1
    print()
    row=row+1

