def for_X(m,n):
    """
        we are creating static python static function to display alphabet X with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (i==0 and j==0)or (i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3)or (i==4 and j==4) or (i==5 and j==5)or (i==6 and j==6) or(j==6 and i==0)or (j==5 and i==1)or (j==4 and i==2)or(j==3 and i==3)or(j==2 and i==4) or(j==1 and i==5)or(j==0 and i==6):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
