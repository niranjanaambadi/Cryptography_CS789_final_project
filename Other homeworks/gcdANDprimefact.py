#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:00:12 2021

@author: niranjanaambadi
"""

def gcd(a,b):
    assert a>=0 and b>=0 and a+b>0
    while a>0 and b>0:
        if a>=b:
            a=a%b
        else:
            b=b%a
        print(a,b)       
    return max(a,b)

#print(gcd(401040,40000000000))

#Extended Euclidean Algorithm

def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

extended_gcd(10,6)
extended_gcd(7,5)
extended_gcd(391,299)
extended_gcd(239,201)
print(extended_gcd(40000000000,401040))

print(gcd(10,6))

a=gcd(1,1)
x=1//a*1//a
print(x)


#Find LCM using euclid's algorithm
def lcm(a, b):
  assert a >= 0 and b >= 0 and a+b>0
  prod=a*b
  while a>0 and b>0:
        if a>=b:
            a=a%b
        else:
            b=b%a
             
  ans= max(a,b)
  print(ans)
  # Write your code here
  return prod//ans


print("LCM",lcm(5,15))


# Python program to print prime factors

import math

# A function to print all prime factors of
# a given number n
def primeFactors(n):
	
	# Print the number of two's that divide n
	while n % 2 == 0:
		print( 2)
		n = n / 2
		
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i and divide n
		while n % i== 0:
			print(i)
			n = n / i
			
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		print (n)
		
# Driver Program to test above function
print("Prime factors\n")
n = 737
primeFactors(n)

# This code is contributed by Harshit Agrawal



