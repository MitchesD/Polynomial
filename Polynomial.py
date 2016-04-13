#!/usr/bin/python3

import math
import copy
from itertools import zip_longest

class Polynomial:
    # function to get max index
    def getMaxIndex(self, kwargs):
        maxValue = 0
        for key, value in kwargs.items():
            if (int(key[1:]) > maxValue):
                maxValue = int(key[1:])
        return maxValue

    # constructor which handles all input arguments
    def __init__(self, *args, **kwargs):
        self.coeffs = []
        
        # parse input arguments
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

    # override string "operator" which provides option to print object in specific format
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

    # override operator "+" to get sum of two polynoms represented by two objects
    def __add__(self, other):
        return Polynomial([a + b for a, b in zip_longest(self.coeffs, other.coeffs, fillvalue=0)])

    # auxiliary method for multiplying polynoms
    def multiply(self, s, v):
        res = [0]*(len(s)+len(v)-1)
        for selfpow,selfcoeff in enumerate(s):
            for valpow,valcoeff in enumerate(v):
                res[selfpow+valpow] += selfcoeff*valcoeff

        return res

    # override operator "**" to pow polynom of M members on N exponent
    def __pow__(self, exp):
        # make a copy of coefficients to be able to multiple together with base coefficients
        self.result = copy.deepcopy(self.coeffs)
        for i in range(1, exp):
            self.result = self.multiply(self.coeffs, self.result)
        
        return Polynomial(self.result)

    # derivate polynom
    def derivative(self):
        new_list = [self.coeffs[i] * i for i in range(1, len(self.coeffs))]
        return Polynomial(new_list)

    # use val in polynom instead of "x" to get exact result
    def getListWithValue(self, val):
        return [value*val**key for key, value in enumerate(self.coeffs)]

    # get value according to given argument(s), returning exact result, using argument instead of variable
    def at_value(self, *args):
        if (len(args) == 1):
            return sum(self.getListWithValue(int(args[0])))
        elif (len(args) == 2):
            return sum(self.getListWithValue(int(args[1]))) - sum(self.getListWithValue(int(args[0])))
        else:
            print("Invalid input arguments in method at_value()")

