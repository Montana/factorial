#! /usr/local/bin/python3.6

import sys
import traceback

class CalcFactorial:
    L = 64 
    L2 = int((L + 7) / 8) 
    N = 49 

    def compute(self):
        try:
            s = [0 for _ in range(self.L2)]
            s[-1] = 1
            for k in range(1, self.N + 1):
                s = self.__long_mul(s, k)
                self.__display(k, s)
        except Exception as e:
            raise

    def __long_mul(self, a, b):
        try:
            z = [0 for _ in range(self.L2)]
            carry = 0
            for i in reversed(range(self.L2)):
                w = a[i]
                z[i] = (w * b + carry) % 100000000
                carry = int((w * b + carry) / 100000000)
            return z
        except Exception as e:
            raise

    def __display(self, k, s):
        try:
            print("{:2d}!=".format(k), end="")
            for i in range(0, self.L2):
                print("{:08d}".format(s[i]), end="")
            print()
        except Exception as e:
            raise

if __name__ == '__main__':
    try:
        obj = CalcFactorial()
        obj.compute()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
