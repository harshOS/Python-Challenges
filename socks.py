import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    i = 0
    pairs = 0

    ar.sort()
    while i < n:
        count += ar.count(ar[i])
        i += count
        pairs += int(count / 2)
        count = 0
    return pairs

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
print(sockMerchant(8, [1,1,1,1,1,1,2,2]))


