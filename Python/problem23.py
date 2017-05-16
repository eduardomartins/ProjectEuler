# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem23.py
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
#  Non-abundant sums
#
#  A perfect number is a number for which the sum of its proper divisors is exactly equal
#  to the number. For example, the sum of the proper divisors of 28 would be
#  1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#  A number n is called deficient if the sum of its proper divisors is less than n and it is
#  called abundant if this sum exceeds n.
#  As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
#  that can be written as the sum of two abundant numbers is 24. By mathematical
# analysis, it can be shown that all integers greater than 28123 can be written as the sum
# of two abundant numbers. However, this upper limit cannot be reduced any further by
# analysis even though it is known that the greatest number that cannot be expressed as
# the sum of two abundant numbers is less than this limit.
#  Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def divisors(n):
    factors = set()
    for div in range(2, n/2):
        if n % div == 0:
            factors.add(div)
            factors.add(n/div)

    if any(factors):
        factors.add(1)

    return sum(factors)


def main():
    s = 0
    abundant = set()
    for n in range(1, 20162):
        if divisors(n) > n:
            abundant.add(n)
        if not any((n-abn in abundant) for abn in abundant):
            s += n
    print s


if __name__ == '__main__':
    main()
