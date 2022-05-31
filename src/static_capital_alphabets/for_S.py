def for_S(m,n):
    """
        we are creating static python static function to display alphabet S with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (i==0 and j!=0) or (i==3 and j!=0 and j!=5)or (i==6 and j!=5) or(i==1 and j==0) or (i==2 and j==0) or (i==4 and j==5) or (i==5 and j==5):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
