# Uses python3
import sys

def euclid_gcd(num1, num2):
    """
    Task: Given two integers a and b, find their greatest common divisor
    """
    if num2 == 0:
        return num1
    num1_remainder = num1 % num2
    return euclid_gcd(num2, num1_remainder)

if __name__=="__main__":
    inp = sys.stdin.read()
    a, b = map(int, inp.split())
    print(euclid_gcd(a, b))