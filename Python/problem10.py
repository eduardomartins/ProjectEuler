#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem10.py
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
#  Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import ceil, sqrt

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


def main():
    print sum(SieveOfAtkin(2000000).getPrimes())


if __name__ == '__main__':
    main()
