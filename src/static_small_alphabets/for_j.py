def for_j(m,n):
    """
        we are creating static python static function to display alphabet j with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==2 and i!=1 and i!=5)or (i==2 and j==1)or(i==5 and j==1)or(i==4 and j==0):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
