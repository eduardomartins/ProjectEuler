#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem4.py
#
#  Copyright 2017 Eduardo Sant'Anna Martins <eduardo@eduardomartins.site>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  ==========================================================
#  Smallest multiple
#
 #  2520 is the smallest number that can be divided by each of the numbers from 1 to 10
 #   without any remainder. What is the smallest positive number that is evenly divisible
 #   by all of the numbers from 1 to 20?

from math import sqrt, ceil, pow
from functools import reduce
import operator

mul = lambda num: reduce(operator.mul, num, 1)

class SieveOfAtkin:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.sieve = [False]*(self.limit+1)

    def flip(self, prime):
        try:
            self.sieve[prime] = True if self.sieve[prime] == False else False
        except KeyError:
            pass

    def invalidate(self, prime):
        try:
            if self.sieve[prime] == True:
                self.sieve[prime] = False
        except KeyError:
            pass


    def isPrime(self, prime):
        try:
            return self.sieve[prime]
        except KeyError:
            return False


    def getPrimes(self):
        testingLimit = int(ceil(sqrt(self.limit)))

        for i in range(testingLimit):
            for j in range(testingLimit):
                # n = 4*i^2 + j^2
                n = 4*int(pow(i, 2)) + int(pow(j,2))
                if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
                    self.flip(n)

                # n = 3*i^2 + j^2
                n = 3*int(pow(i, 2)) + int(pow(j,2))
                if n <= self.limit and n % 12 == 7:
                    self.flip(n)

                # n = 3*i^2 - j^2
                n = 3*int(pow(i, 2)) - int(pow(j,2))
                if n <= self.limit and i > j and n % 12 == 11:
                    self.flip(n)


        for i in range(5, testingLimit):
            if self.isPrime(i):
                k = int(pow(i, 2))
                for j in range(k, self.limit, k):
                    self.invalidate(j)

        self.primes = [2, 3] + [x for x in range(len(self.sieve)) if self.isPrime(x) and x>=5]
        return self.primes


def last_common_multiple(limit):
    append = False
    lcm = []
    primes = SieveOfAtkin(limit).getPrimes()
    numbers = range(1, limit+1)
    while(mul(numbers) > 1):
        for prime in primes:
            aux = []
            for num in numbers:
                if num % prime == 0:
                    aux.append(num / prime)
                    if not append:
                        lcm.append(prime)
                        append = True
                else:
                    aux.append(num)
            numbers = aux
            append = False
            print numbers, " | ",  lcm[-1]
            if mul(numbers) == 1:
                return mul(lcm)
    return mul(lcm)

def main():
    resp = last_common_multiple(20)
    print 'Resposta: ', resp
    return 0

if __name__ == '__main__':
    main()
