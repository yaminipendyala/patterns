def for_v(m,n):
    """
        we are creating static python static function to display alphabet v with representation of "*"(star) by using for loop.
    parameters:
    m:It represents number of rows in the matrix
    n:It represents number of columns in the matrix
    """
    for i in range(m):
        for j in range(n):
            if  i+j ==6 or i-j == 0:
                print("*",end="")
            else:
                 print(" ",end="")
        print()
