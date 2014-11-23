#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# problem3.py
#  
#  Copyright 2014 Eduardo Sant'Anna Martins <eduardomartins993@hotmail.com>
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
#  ===================================================================
#  Largest prime factor
#  Problem 3
#  The prime factors of 13195 are 5, 7, 13 and 29.
#  What is the largest prime factor of the number 600851475143 ?


def prime(n):
    if n == 1 or n == 2:
        return True
    k = 2
    while k < n / 2 and n % k != 0:
        k += 1
    else:
        return True
    return False


def largest_prime_factor(n):
    k = 2
    while k <= n:
        print n, k
        if prime(k) and n % k == 0:
            n /= k
            if n == 1:
                return k
        k += 1

    return False


def main():
    num = 600851475143
    print 'The largest factor prime is:', num, largest_prime_factor(num)
    return 0


if __name__ == '__main__':
    main()

