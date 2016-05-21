# Walter Sagehorn
# PE problem 6
# 5/1/2016

def fact(num):
    x = 1
    for i in range(1, num+1):
        x *= i
    return x

def sum(num):
    x = 0
    for i in range(0, num+1):
        x += i
    return x

def sumsq(num):
    x = 0
    for i in range(0, num+1):
        x += i*i
    return x

def main():
    print sum(100) * sum(100) - sumsq(100)

if __name__ == '__main__':
    main()
