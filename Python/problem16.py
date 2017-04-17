#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem16.py
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
#  Power digit sum
#  2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#  What is the sum of the digits of the number 2^1000?


def main():
    number = str(2**1000)
    result = sum([int(num) for num in number])
    print result


if __name__ == '__main__':
    main()
