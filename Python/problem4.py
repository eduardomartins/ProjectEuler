#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem4.py
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
#  Largest palindrome product
#  Problem 4
#
#  A palindromic number reads the same both ways. The largest palindrome
#  made from the product of two 2-digit numbers is 9009 = 91 × 99.
#  Find the largest palindrome made from the product of two 3-digit numbers.



def palindromic(x, y):
    return str(x * y) == str(x * y)[::-1]


def largest_palindromic(n=100, k=999):
    num = 0
    for i in xrange(k, n, -1):
        for x in xrange(k, n, -1):
            if palindromic(i, x) and i * x > num:
                num = i * x
    return num


def main():
    print largest_palindromic()
    return 0

if __name__ == '__main__':
    main()

