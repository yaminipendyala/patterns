def for_y(m,n):
    """
        we are creating static python static function to display alphabet y with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if j==4 or j==0 and i in(0,1,2,5) or (i==3 and j!=0)or (i==6 and j!=0):
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print() 
