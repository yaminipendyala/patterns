def for_C(m,n):
    """
        we are creating static python static function to display alphabet C with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if i==0 and j!=0 or i==6 and j!=0 or (j==0 and i not in (0,6)):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
