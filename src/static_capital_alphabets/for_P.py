def for_P(m,n):
    """
        we are creating static python static function to display alphabet P with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0 and i!=6)or (i==0 and j!=4) or (i==3 and j!=4) or (i==1 and j==4) or (i==2 and j==4):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
