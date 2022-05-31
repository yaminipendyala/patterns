def for_q(m,n):
    """
        we are creating static python static function to display alphabet q with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==3)or(i==0 and j not in(0,4,5))or(j==0 and i not in(0,3,4,5,6))or (i==3 and j not in(0,4,5))or(i==3 and j not in(0,1,2,4,5))or(i==5 and j==4):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
