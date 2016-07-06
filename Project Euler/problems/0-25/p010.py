# Walter Sagehorn
# PE problem 10
# 7/5/2016

from utilities import primes_below



def main():
    print sum(primes_below(2 * 1000 * 1000))

if __name__ == '__main__':
    main()