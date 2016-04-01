#!/usr/bin/python

import re
from itertools import izip_longest

class Polynomial:
    def parseArg(arg):
        return

    def __init__(self, *args):
        self.coeffs = []
        for arg in args:
            if isinstance(arg, list):
                self.coeffs.extend(arg)
            elif isinstance(arg, int):
                self.coeffs.append(arg);
            else:
                self.parseArg(arg)

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
        return Polynomial([a + b for a, b in izip_longest(self.coeffs, other.coeffs, fillvalue=0)])


print (Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))

