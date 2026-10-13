def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    n = len(a)
    m = len(a[0])
    # print(n,m)
    transpose = []
    for i in range(m):
        row = []
        for j in range(n):
            # print(j,i)
            row.append(a[j][i])
        transpose.append(row)
    return transpose
    pass