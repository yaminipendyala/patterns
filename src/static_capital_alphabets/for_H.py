def for_H(m,n):
    """
        we are creating static python static function to display alphabet H with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (i==3) or (j==0 or j==4):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
