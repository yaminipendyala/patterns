def for_G(m,n):
    """
        we are creating static python static function to display alphabet A with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==0 and i!=6) or (i==0 and j!=5)or (i==6 and j!=5 and j!=0)or(j==4 and i in(3,4,5))or(i==3 and j in (3,4,5)):
                print('*', end="")
            else:
                print(" ",end="")
        print()
