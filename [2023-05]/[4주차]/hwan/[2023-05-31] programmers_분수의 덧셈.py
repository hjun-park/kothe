# 내가 푼 것

import math
from fractions import Fraction


def solution(numer1, denom1, numer2, denom2):
    answer = []
    lcm = 0
    lst = []

    for i in range(max(denom1, denom2), (denom1 * denom2) + 1):
        if i % denom1 == 0 and i % denom2 == 0:
            lcm = i
            break

    numer1 *= int(lcm / denom1)
    numer2 *= int(lcm / denom2)

    lst.append(numer1 + numer2)
    lst.append(lcm)

    gcd = math.gcd(lst[0], lst[1])

    answer.append(lst[0]/gcd)
    answer.append(lst[1]/gcd)
    return answer

solution(9,2,1,3)

# fractions 함수

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

#numerator 은 분자, denominator 은 분모