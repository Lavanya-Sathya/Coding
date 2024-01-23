def countDigit(n):
    count = 0
    while n!=0:
        count += 1
        n = n // 10
    return count
if __name__ == "__main__":
    n = 123434
    count = countDigit(n)
    print("Count Digit: ", count)