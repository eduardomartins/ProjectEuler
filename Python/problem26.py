# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem26.py
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
# Reciprocal cycles
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import re
from decimal import Decimal, getcontext

comp = re.compile("(?:0.0*)(\d+)")
getcontext().prec = 2048

def get_pattern(string):
    formated = ''.join(comp.findall(string))
    slice = ''
    for index, char in enumerate(formated):
        slice += char
        if len(slice) > 1:
            if formated.find(slice, index+1) != -1:
                sub = formated.find(slice, index+1)
                if sub == index + 1:
                    return slice
            else:
                slice = ''
    return None


def main():
    d = 2
    index = None
    count = 0
    fraction = None
    while d < 1000:
        fraction = Decimal(1)/Decimal(d)
        pattern = get_pattern(str(fraction))
        if pattern and count < len(pattern):
            count = len(pattern)
            index = d
        d += 1
    print 'RESPONSE: ', index, "TOTAL: ", count


if __name__ == '__main__':
    main()
