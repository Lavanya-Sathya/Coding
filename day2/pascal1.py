# Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle
def findValue(n, r):
    temp = 1
    for i in range(r):
        temp = temp * (n-i)
        temp = temp // (i+1)
    return temp

def pascal(r, c):
    res = findValue(r-1,c-1)
    return res

if __name__ == "__main__":
    ans = pascal(4,2)
    print("The result is: ", ans)