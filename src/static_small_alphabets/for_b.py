def for_b(m,n):
    """
        we are creating static python static function to display alphabet b with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0)or(i==3 and j!=3)or(i==6 and j!=3)or j==3 and i not in(0,1,2,3,6):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
