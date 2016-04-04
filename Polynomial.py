#!/usr/bin/python3

import re
import math
import operator
from itertools import zip_longest

class Polynomial:
    def getMaxIndex(self, kwargs):
        maxValue = 0
        for key, value in kwargs.items():
            if (int(key[1:]) > maxValue):
                maxValue = int(key[1:])
        return maxValue

    def __init__(self, *args, **kwargs):
        self.coeffs = []
        for arg in args:
            if isinstance(arg, list):
                self.coeffs.extend(arg)
            elif isinstance(arg, int):
                self.coeffs.append(arg)
        if kwargs:
            maxIndex = self.getMaxIndex(kwargs)
            self.coeffs = [0] * (int(maxIndex) + 1)
            for key, value in kwargs.items():       
                self.coeffs[int(key[1:])] = value

    def __repr__(self):
        return "Polynomial()"

    def __str__(self):
        result = ""

        maxPower = len(self.coeffs) - 1

        for power, item in reversed(list(enumerate(self.coeffs))):
            if (item == 0):
                continue
            
            if (power == maxPower):
                coeff = "" if item > 0 else "-"
            else:
                coeff = " + " if item > 0 else " - "

            coeff += "" if power != 0 and (item == 1 or item == -1) else str(abs(item))

            if (power == 0):
                suf = ""
            elif (power == 1):
                suf = "x"
            else:
                suf = "x^" + str(power)

            result += coeff + str(suf)

        return result

    def __add__(self, other):
        return Polynomial([a + b for a, b in zip_longest(self.coeffs, other.coeffs, fillvalue=0)])

    def binomial_coefficient(self, n, k):
        if (n == 0 or k == 0):
            return 1
        if (k > n):
            return 0
        if (k > (n - k)):
            k = n - k
        if (k == 1):
            return n

        return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

    def __pow__(self, exp):
        result = []
        for i in range(0, exp + 1):
            cexp = exp - i
            bin = self.binomial_coefficient(exp,i) * (self.coeffs[1]**cexp) * (self.coeffs[0]**i)      
            result.insert(i, bin)

        return Polynomial(result)

    def derivative(self):
        new_list = [self.coeffs[i] * i for i in range(1, len(self.coeffs))]
        return Polynomial(new_list)

    def getListWithValue(self, val):
        return [value*val**key for key, value in enumerate(self.coeffs)]

    def at_value(self, *args):
        if (len(args) == 1):
            return sum(self.getListWithValue(int(args[0])))
        elif (len(args) == 2):
            return sum(self.getListWithValue(int(args[1]))) - sum(self.getListWithValue(int(args[0])))
        else:
            print("Invalid input arguments in method at_value()")


#pol1 = Polynomial([1,-3,0,2])
#pol2 = Polynomial(1,-3,0,2)
#pol3 = Polynomial(x0=1,x3=2,x1=-3)

#print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))

#print(pol1)
#print(pol2)
#print(pol3)

#print(pol1.derivative())
#print(pol1.at_value(2,3))

print(Polynomial(1, 1) ** 5)

