def for_Q(m,n):
    """
        we are creating static python static function to display alphabet Q with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0 and i not in (0,7))or (j==4 and i not in (0,7))or(i==0 and j not in(0,4))or(i==7 and j not in(0,4)):
                print('*', end=" ")
            else:
                print(" ",end=" ")
        print()
