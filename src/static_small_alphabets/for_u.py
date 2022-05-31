def for_u(m,n):
    """
        we are creating static python static function to display alphabet u with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0 and i!=3) or (j==3 and i!=3) or i==3 and j not in (0,3):
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print() 
