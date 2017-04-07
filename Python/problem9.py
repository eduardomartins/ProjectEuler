#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem9.py
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
#   Special Pythagorean triplet
#
#   A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                                                            a^2 + b^2 = c^2
#
#  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc.


def special_pythagorean_triplet(s = 1000):
    a = 1
    b = a + 1
    while(a < b):
        b = a + 1
        c = s - a - b
        while(b < c):
            c = s - a - b
            if(a**2 + b**2 == c**2):
                return (a, b, c,  a*b*c)
            b += 1
        a += 1


if __name__ == '__main__':
    print special_pythagorean_triplet()
