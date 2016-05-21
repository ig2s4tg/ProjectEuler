# Walter Sagehorn
# PE problem 7
# 5/1/2016


def is_prime(num, list):
    for i in list:
        if (num % i == 0):
            return False
        if (i > num / 2 ):
            return True
    return True

def main():
    l = [2,3,5,7]
    i = 11
    while (len(l) <= 10001):
        if is_prime(i, l):
            l.append(i)
        i += 2
    print l[len(l)-2]

if __name__ == '__main__':
    main()