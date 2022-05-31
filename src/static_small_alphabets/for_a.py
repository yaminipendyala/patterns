def for_a(m,n):
    """
        we are creating static python static function to display alphabet a with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==4 and i!=0)or(i==0 and j not in (0,4))or(j==0 and i not in(0,2,3,6))or(i==3 and j!=0)or(i==6 and j!=0):
                print('*', end=' ')
            else:
                print(" ",end=" ")
        print()
