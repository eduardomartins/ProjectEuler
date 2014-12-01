#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem6.py
#  
#  Copyright 2014 Eduardo Sant Anna Martins <eduardomartins993@hotmail.com>
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
#  ==================================================================
#  Sum square difference
#  Problem 6
#
#  The sum of the squares of the first ten natural numbers is,
#               1² + 2² + ... + 10² = 385
#
#  The square of the sum of the first ten natural numbers is,
#            (1 + 2 + ... + 10)² = 55² = 3025
#
#  Hence the difference between the sum of the squares of the first ten
#  natural numbers and the square of the sum is 3025 − 385 = 2640.
#  Find the difference between the sum of the squares of the first one
#  hundred natural numbers and the square of the sum.


def get_term(n):
    if n <= 1:
        return
    else:
        return get_term(n-1) + (2*n - 1)



def main():
    for i in range(1, 11):
        print get_term(i)
    return 0

if __name__ == '__main__':
    main()

