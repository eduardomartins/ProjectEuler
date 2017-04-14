#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem12.py
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
#  Highly divisible triangular number
#  The sequence of triangle numbers is generated by adding the natural numbers.
#  So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
#  terms would be:
#                                          1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#      10: 1,2,5,10
#      15: 1,3,5,15
#      21: 1,3,7,21
#      28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
import sys, time

start_time = time.time()


def factors_primes(num, primes):
    total = 1
    factor = []
    factors = 1

    for prime in primes:
        while num % prime == 0:
            factor.append(prime)
            num /= prime
            total += 1

        if total > 1:
            factors *= total

        total = 1

        if prime > num:
            break

    return (factors, factor)


def triangle_numbers(n):
    return n*(n+1)/2

def primes_numbers(nth):
    total = 1
    num = 3
    primes = [2, ]
    is_prime = True

    while total <= nth:
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            total += 1
            primes.append(num)
        else:
            is_prime = True

        num += 1

    return primes


def main(n):
    total = 0
    index = n
    factors = []
    primes = primes_numbers(index)
    triangle = triangle_numbers(index)

    while total <= n:
        index += 1
        triangle += index
        total, factors = factors_primes(triangle, primes)

    print 'nth=%s, triangle=%s, total divisors=%s, factors=%s' % (index, triangle, total, factors)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <number>' % sys.argv[0]
    else:
        num = sys.argv[1]
        main(int(num))
        print "Elapsed Time: ", time.time() - start_time, "second(s)" 