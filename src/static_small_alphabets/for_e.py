def for_e(m,n):
    """
        we are creating static python static function to display alphabet e with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(7):
        for j in range(5):
            if (i==0 and j!=0 and j!=4) or i==3 or (j==0 and i!=0 and i!=6) or (i==6 and j!=0) or (i==1 and j==4 and i!=0) or(i==2 and j==4):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
