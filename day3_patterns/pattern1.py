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


if __name__ == "__main__":
    n = 5
    SqrPattern(n)
    triPattern(n)
    triNumPattern(n)
    triRowNumPattern(n)
    reverseTriPattern(n)
    reverseTriNumPattern(n)
