#!/bin/python3

import math
import os
import random
import re
import sys


def missingCharacters(s):
    # Write your code here
    l = [0]*123
    result=""
    for i in range(len(s)):
        x=ord(s[i])
        l[x]+=1
        for i in range(48,58):
            if(l[i]==0):
                result+=chr(i)
                for i  in range (97,123):
                    if(i[i]==0):
                        result+=char(i)
                        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()