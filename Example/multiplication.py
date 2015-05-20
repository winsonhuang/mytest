for i in range(1, 10):
    for j in range(1, i + 1):
        k= i * j
        if i * j < 10:
            k=str(i * j)+ " "
        print '%d x %d = %s  '% (i, j, k),
    print