# Square pattern print
def SqrPattern(n):
    print("square pattern ")
    for i in range(n):
        for j in range(n):
            print("* ", end=" ")
        print()

# triangle pattern print
def triPattern(n):
    print("Triangle pattern ")
    for i in range(n):
        for j in range(i+1):
            print("* ", end=" ")
        print()

# Triangle number pattern
def triNumPattern(n):
    print("Triangle number pattern ")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# Triangle row number pattern
def triRowNumPattern(n):
    print("Triangle row number pattern ")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

def reverseTriPattern(n):
    print("Reverse Triangle pattern ")
    for i in range (n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()

# Reverse Triangle Number pattern 
def reverseTriNumPattern(n):
    print("Reverse Triangle Number pattern ")
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j , end=" ")
        print()

# triangle pattern
def patternTriangle(n):
    print("Triangle pattern ")
    for i in range(n, 0, -1):
        l= n-i+1
        for j in range(0, i-1):
            print(" ", end=" ")
        for k in range(0,l):
            print("*", end=" ")
        for m in range(l-1):
            print("*",end=" ")
        print() 

def patternReverseTriangle(n):
    print("Reverse Triangle pattern ")
    for i in range(n):
        l = n - i
        for j in range(i):
            print(" ",end=" ")
        for k in range(l):
            print("*", end=" ")
        for k in range(l-1):
            print("*", end=" ")
        print()

# diamond Pattern
def diamondPattern(n):
    print("Diamond Pattern")
    for i in range(n, 0, -1):
        l = n -i +1
        for j in range(i-1):
            print(" ", end=" ")
        for k in range(l):
            print("*",end=" ")
        for m in range(l-1):
            print("*",end=" ")
        print()
    for i in range(n):
        l = n -i
        for j in range(i):
            print(" ",end=" ")
        for k in range(l):
            print("*",end=" ")
        for m in range(l-1):
            print("*",end=" ")
        print()

# tenth pattern
def tenthPattern(n):
    print("Tenth pattern")
    for i in range(1,n+1):
        for j  in range(i):
            print("*",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

# eleventh Pattern
def eleventhPattern(n):
    print("eleventh Pattern")
    temp = 1
    for i in range(1,n+1):
        for j in range(i):
            print(temp, end=" ")
            if temp == 1:
                temp = 0
            else: 
                temp = 1
            # print("temp", temp)
        print()

# Pattern12
def Pattern12(n):
    print("Pattern 12")
    for i in range(1, n+1):
        l = n-i
        for j in range(1,i+1):
            print(j,end=" ")
        for k in range(l):
            print(" ",end=" ")
        for k in range(l):
            print(" ",end=" ")
        for j in range(i, 0 ,-1):
            print(j,end=" ")
        print()


# Pattern13
def Pattern13(n):
    print("Pattern 13")
    temp = 1
    for i in range(1, n+1):
        for j in range(i):
            print(temp, end=" ")
            temp = (temp) + 1
        print()

# Pattern14(n)
def Pattern14(n):
    print("Pattern 14")
    temp = ord("A")
    for i in range(1,n+1):
        for j  in range(i):
            print(chr(temp),end=" ")
            temp += 1
        temp = ord("A")
        print()

# Pattern15(n)
def Pattern15(n):
    print("Pattern 15")
    temp = ord("A")
    for i in range(n, 0 ,-1):
        for j in range(i):
            print(chr(temp),end=" ")
            temp+=1
        temp = ord("A")
        print()
# Pattern 16
def Pattern16(n):
    print("Pattern 16")
    temp = ord("A")
    for i in range(n):
        for j in range(i+1):
            print(chr(temp),end=" ")
        temp+=1
        print()
# Pattern17
def Pattern17(n):
    print("Pattern 17")
    temp = ord("A")
    for i in range(1, n+1):
        l = n-i
        for j in range(l):
            print(" ",end=" ")
        for k in range(i):
            print(chr(temp),end=" ")
            temp+=1
        temp = ord("A") + (i-2)
        for m in range(i-1):
            print(chr(temp),end=" ")
            temp -= 1
        temp = ord("A")
        print()
            
# pattern 18
def Pattern18(n):
    print("Pattern 18")
    temp = ord("A") + n-1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(temp), end=" ")
            temp+=1
        temp = ord("A") + (n-i-1)
        print()

#pattern 19
def Pattern19(n):
    print("Pattern 19")
    for i in range(n,0,-1):
        l=n-i
        for j in range(i):
            print("*",end=" ")
        for k in range(l):
            print(" ",end=" ")
        for k in range(l):
            print(" ",end=" ")
        for m in range(i):
            print("*",end=" ")
        print()
    for i in range(n):
        l=n-i
        for j in range(i+1):
            print("*",end=" ")
        for k in range(l-1):
            print(" ",end=" ")
        for k in range(l-1):
            print(" ",end=" ")
        for m in range(i+1):
            print("*",end=" ")
        print()
# pattern 20
def Pattern20(n):
    print("Pattern 20")
    for i in range(n):
        l= n-i
        for j in range(i+1):
            print("*",end=" ")
        for k in range(l-1):
            print(" ",end=" ")
        for k in range(l-1):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n,0,-1):
        l = n-i+1
        for j in range(i):
            print("*",end=" ")
        for k in range(l-1):
            print(" ",end=" ")
        for k in range(l-1):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
# pattern 21
def Pattern21(n):
    print("Pattern 21")
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i == 1 or i== n:
                print("*",end=" ")
            elif j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()

if __name__ == "__main__":
    n = 5
    SqrPattern(n)
    triPattern(n)
    triNumPattern(n)
    triRowNumPattern(n)
    reverseTriPattern(n)
    reverseTriNumPattern(n)
    patternTriangle(n)
    patternReverseTriangle(n)
    diamondPattern(n)
    tenthPattern(n)
    eleventhPattern(n)
    Pattern12(n)
    Pattern13(n)
    Pattern14(n)
    Pattern15(n)
    Pattern16(n)
    Pattern17(n)
    Pattern18(n)
    Pattern19(n)
    Pattern20(n)
    Pattern21(n)