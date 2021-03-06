#!/usr/bin/env python3

def watermelon(n):
    if n % 2 != 0 or n == 2:
        return False
    return True

if __name__ == "__main__":
     w = int(input())
     
     if watermelon(w):
         print('YES')
     else:
         print('NO')
