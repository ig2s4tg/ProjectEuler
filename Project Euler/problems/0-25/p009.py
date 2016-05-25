# Walter Sagehorn
# PE problem 9
# 5/1/2016

import math

def main():
    for b in range(400):
        for a in range(b):
            c = math.sqrt(a**2 + b**2)
            if (a + b + c == 1000):
                print str(a * b * c)
                exit(0)

if __name__ == '__main__':
    main()
