#!/usr/bin/python

class Polynomial:
    def __init__(self, list):
        self.list = list;

    def __repr__(self):
        return "Polynomial()"

    def __str__(self):
        result = ""

        maxPower = len(self.list) - 1

        for power, item in reversed(list(enumerate(self.list))):
            if (item == 0):
                continue
            
            if (power == maxPower):
                coeff = "" if item > 0 else "-"
                coeff += str(abs(item))
            else:
                coeff = " + " if item > 0 else " - "
                coeff += str(abs(item))

            if (power == 0):
                suf = ""
            else:
                suf = "x^" + str(power)

            result += coeff + str(suf)

        return result

pol2 = Polynomial([1,-3,0,2,10,-5,8,-4])

print(pol2)
