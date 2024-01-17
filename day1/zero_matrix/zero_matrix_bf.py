# mark all the element in row with 0 as -1
def makeMinusOneRow(matrix,n,m,i):
    for k in range(m):
        if(matrix[i][k] != 0):
            matrix[i][k] = -1
            
# mark all the element in col with 0 as -1
def makeMinusOneCol(matrix,n,m,j):  
    for x in range(n):
        if(matrix[x][j] != 0):
            matrix[x][j] = -1

def zeroMatrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                makeMinusOneRow(matrix,n,m,i)
                makeMinusOneCol(matrix,n,m,j)

    # To get the final result make all -1 to 0
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == -1):
                matrix[i][j] = 0
    
    return matrix

if __name__ == "__main__":
    matrix = [[1, 1, 1],[1, 0, 1], [1, 1, 1]]
    n = len(matrix)    # no of row
    m = len(matrix[0]) # no of col
    ans = zeroMatrix(matrix, n, m)
    print("No of rows: " , n)
    print("No of cols: ", m)
    print("The Final matrix is:")

    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()



