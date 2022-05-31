def for_Y(m,n):
    """
        we are creating static python static function to display alphabet Y with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (i==0 and j==0)or (i==1 and j==1) or (i==2 and j==2) or(i==3 and j==3)or(i==2 and j==4) or(i==1 and j==5)or (i==0 and j==6)or(j==3 and i!=0 and i not in (1,2)):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
