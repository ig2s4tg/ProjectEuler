#walter sagehorn
#PE problem 4
#5/1/2016


def isPal(num):
    s = str(num)
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True





def main():
    largest = 0
    for x in range(100, 999):
        for y in range(100, 999):
            if (x * y > largest and isPal(x * y)):
                largest = x * y
    print largest

if __name__ == '__main__':
    main()
