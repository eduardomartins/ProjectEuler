# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem28fa.py
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
# Number spiral diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#                                               21 22 23 24 25
#                                               20 07 08 09 10
#                                               19 06 01 02 11
#                                               18 05 04 03 12
#                                               17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def main(n):
    spiral = ((16 * n**3) + 26 * n)/3 + 10 * n**2
    print spiral + 1


if __name__ == '__main__':
    main(500)
