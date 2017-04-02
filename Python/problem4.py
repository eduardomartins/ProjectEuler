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
#  =========================================================================
#  Largest palindrome product
#
#  A palindromic number reads the same both ways. The largest palindrome made
#  from the product of two 2-digit numbers is 9009 = 91 × 99
#  Find the largest palindrome made from the product of two 3-digit numbers.
#

from math import ceil, floor


def is_palindrome(n):
    num = str(n)
    length = len(num)
    if length % 2 == 0:
        return num[0:length/2] == num[length/2:length][::-1]
    else:
        return num[0:int(floor(length/2.0))] == num[int(ceil(length/2.0)):length][::-1]


def largest_palindrome(digits):
    num = int('9' * digits)
    palindromes = []
    for n in xrange(num, int('9'*(digits-1)), -1):
        for n1 in xrange(num, int('9'*(digits-1)), -1):
            buff = n * n1
            if is_palindrome(buff):
                palindromes.append(buff)

    return max(palindromes)


def main():
    print largest_palindrome(3)
    return 0


if __name__ == '__main__':
    main()
