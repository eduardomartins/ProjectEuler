#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem15.py
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
# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the
# right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


def factorial(n):
    product = 1
    for num in xrange(1, n+1):
        product *= num
    return product


def combinatorics(n, i):
    if n >= i:
        return factorial(n)/(factorial(i) * factorial(n - i))
    else:
        raise ValueError(' %s must be equal or less than %s' % (i, n))


def main():
    num = 20
    print "({0} x {0}) = {1}".format(num, combinatorics(2*num, num))


if __name__ == '__main__':
    main()
