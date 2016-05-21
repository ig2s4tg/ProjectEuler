# Walter Sagehorn
# PE problem 5
# 5/1/2016

def is_div(num):
    for i in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 7]:
        if num % i != 0:
            return False
    return True


def main():
    x = 1
    while x < 1000000000:
        if (x % 1000000 == 1): print x
        if is_div(x):
            print x
            break
        x += 1

if __name__ == '__main__':
    main()
