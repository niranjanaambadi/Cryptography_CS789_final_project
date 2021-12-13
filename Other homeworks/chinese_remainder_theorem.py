#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:43:14 2021

@author: niranjanaambadi
"""

def ExtendedEuclid(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = ExtendedEuclid(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)



#Chinese remainder theorem
def ChineseRemainderTheorem(n1, r1, n2, r2):
  (d,x, y) = ExtendedEuclid(n1, n2)
 
  m = n1 * n2
  n = r2 * x * n1 + r1 * y * n2
  return (n % m + m) % m


print(ChineseRemainderTheorem(3,5,1,7))