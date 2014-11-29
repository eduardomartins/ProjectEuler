#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem5.py
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
#  Smallest multiple
#  Problem 5
#
#  2520 is the smallest number that can be divided by each of the numbers
#  from 1 to 10 without any remainder.What is the smallest positive number
#  that is evenly divisible by all of the numbers from 1 to 20?


def greatest_common_divisor(a, b, *args):
    if bool(args):
        args = list(args)
        return greatest_common_divisor(greatest_common_divisor(a, b), args.pop(0), *args)
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def least_common_multiple(*args):
    lcm = 1
    for i in args:
        lcm = (i * lcm)/greatest_common_divisor(i, lcm)
    return lcm


def main():
    print least_common_multiple(*range(1, 21))
    return 0


if __name__ == '__main__':
    main()

