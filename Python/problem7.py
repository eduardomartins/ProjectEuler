#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem7.py
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
#  10001st prime
#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th
#   prime is 13. What is the 10 001st prime number?

def prime(n):
    count = 1
    primes = [2, ]
    is_prime = True
    num = 3

    while(count < n):
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            count += 1
        else:
            is_prime = True

        num += 1

    return primes[-1]



def main():
    result = prime(10001)
    print result


if __name__ == '__main__':
    main()
