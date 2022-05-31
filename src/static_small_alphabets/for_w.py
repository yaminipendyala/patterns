def for_w(m,n):
    """
        we are creating static python static function to display alphabet w with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0 and i!=4) or (j==6 and i!=4) or (j==3 and i not in(0,1,4))or (i==4 and j!=0 and j!=3 and j!=6):
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print() 
