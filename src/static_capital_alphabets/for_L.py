def for_L(m,n):
    """
        we are creating static python static function to display alphabet L with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0) or(i==6):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()