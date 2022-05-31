def for_r(m,n):
    """
        we are creating static python static function to display alphabet r with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if (j==2 and i!=0) or i==0 and j not in (0,2):
                print("*",end=" ")
            else:
                 print(" ",end=" ")
        print()
