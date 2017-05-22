# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem27.py
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
# Quadratic primes
#
# Euler discovered the remarkable quadratic formula:
#
#                                          n2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0≤n≤39
# . However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41,
# and certainly when n=41,41^2+41+41
#
# is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
#
# . The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
#     n^2+an+b
#
# , where |a|<1000 and |b|≤1000
#
# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
#
# Find the product of the coefficients, a
# and b, for the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with n=0.


def is_prime(n):
    for factor in xrange(2, abs(n)/2):
        if n % factor == 0:
            return False
    return True


def main():
    n = 0
    product = [0, 0, 0]

    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            while is_prime(n**2 + n*a + b):
                #print "n = %d  a = %d b = %d " % (n, a, b)
                n += 1

            if n >= product[0]:
                product = [n, a, b]

            n = 0

    print "N = %d and %d * %d = %d" % tuple(product + [product[1] * product[2]])


if __name__ == '__main__':
    main()
