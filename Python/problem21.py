# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem21.py
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
# Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
# divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a
# and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.


def divisors(n):
    result = [1]

    for div in range(2, n/4):
        if n % div == 0 and not(div in result):
            result.append(div)
            other = n/div
            if not(other in result):
                result.append(other)

    return sum(result)


def main():
    amicable = []
    for num in range(2, 10001):
        other = divisors(num)
        back = divisors(other)
        if num != other and num == back:
            amicable.append(num)

    print amicable, sum(amicable)


if __name__ == '__main__':
    main()
