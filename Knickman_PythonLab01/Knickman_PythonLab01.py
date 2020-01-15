#Andrew Knickman
#ITEC 345
#Python Lab 1

#Hailstone Sequence
#Area of Circle
#Range of Character Pair
#Range of Numeric Pair
#Eratosthanes Sieve

import math
import string
import re

def hailstone(n):
    print(n)
    if n == 1:
        print("...")
    elif n % 2 == 0:
        return hailstone(n // 2)
    else:
        return hailstone((3 * n) + 1)

#Area of Circle
def aoc(r):
    print("\nArea of Circle (R=" + str(r) + ")")
    a = math.pi * (math.pow(r, 2))
    print(a)
    

#Range of Character Pair
def rangeCharPair(a,b):
    print("\nCharacter Range (" + a + " to " + b + ")")
    for i in range(ord(a),ord(b)+1):
        print(chr(i))
    
    
#Range of Numeric Pair
def rangeNumrPair(x,y):
    print("\nNumeric Range (" + str(x) + "," + str(y) + ")")
    for i in range(x,y+1):
        print(i)
    
    
#Eratosthenes Sieve
def esieve(n):
    print("\nEratosthenes Sieve (1-" + str(n) + ")")
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            print(p) 
    

print("FUNCTION TESTS")
print("\nHailstone Sequence")
print(hailstone(3))
print(aoc(5.0))
print(rangeCharPair('A','F'))
print(rangeNumrPair(1,10))
print(esieve(10))

fname = "Python Lab1.txt"
f = open(fname,"r")

print("\nREADING: " + fname + "\n")

for line in f:
    print("\n" + line)
    if "HailStone:" in line:
        a = re.findall('\d+',line)
        print(hailstone(int(a[0])))
    elif "Alpha Rng:" in line:
        b = line.split()
        print(rangeCharPair(b[2],b[3]))
    elif "Numeric R:" in line:
        c = re.findall('\d+',line)
        print(c)
        print(rangeNumrPair(int(c[0]),int(c[1])))
    elif "Circle-ra:" in line:
        r = re.findall('\d+',line)
        print(aoc(int(a[0])))
    elif "Eratoshe:" in line:
        e = re.findall('\d+',line)
        print(e)
        print(esieve(int(e[0])))