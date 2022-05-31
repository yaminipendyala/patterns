def for_t(m,n):
    """
        we are creating static python static function to display alphabet t with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if j==1  or i==2 or j==2 and i==5:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print()
