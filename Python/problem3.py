#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem3.py
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


def prime(n, k=2):
    if n == 1 or n == 2:
        return True
    if k < n/2:
        if n % k != 0:
            return prime(n, k+1)
        else:
            return False
    else:
        return True


def largest_prime_factor(n, k=2):
    if n == 1:
        return k

    if prime(k) and n % k == 0:
        return largest_prime_factor(n/k, k)
    else:
        return largest_prime_factor(n, k+1)


def main():
    print largest_prime_factor(13195)

if __name__ == '__main__':
    main()

