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
# Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

import sys


def collatz_sequence(n, verbose=False):
    count = 1
    while n > 1:
        if verbose:
            sys.stdout.write("%s->" % n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    if verbose:
        print 1
    return count

def main():
    n = 1
    count = 0
    largest = 0
    number = None

    while n < 10**6:
        count = collatz_sequence(n)
        if count > largest:
            largest = count
            number = n
        n += 1
        
    print 'LARGEST', largest, number


if __name__  == '__main__':
    main()
