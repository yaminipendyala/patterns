def for_m(m,n):
    """
        we are creating static python static function to display alphabet m with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0)or(j==2 and i!=0)or(j==4 and i!=0)or(i==0 and j!=2 and j!=4):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
