# function to make matrix zero
def zeroMatrix(matrix, n, m):
    # two arrays one of size row and other of size column
    row = [0] * n
    col = [0] * m

    # Traverse the matrix and mark the row & col array with 1 if matrix element is zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    # for i in range(n):
    #     if row[i] == 1:
    #         for j in range(m):
    #             matrix[i][j] = 0

    # for j in range(m):
    #     if col[j] == 1:
    #         for i in range(n):
    #             matrix[i][j] = 0
    
    # To get the result matrix mark (i,j) to zero
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
    
    return matrix

    
if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)

    print("The Final Matrix is: ")

    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()
