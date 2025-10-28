def pascal(n):
    for i in range(n):
        print(" "*(n-i-1)+"* "*(i+1))
rows=int(input("ENTER NUMBER OF ROWS: "))
pascal(rows)