def for_f(m,n):
    """
        we are creating static python static function to display alphabet f with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (i==0 and j!=0 and j!=1 and j!=6) or (j==1 and i!=0) or(i==2) :
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
