# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem24.py
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
# Lexicographic permutations
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically
# or alphabetically, we call it lexicographic order. The lexicographic permutations
# of 0, 1 and 2 are:
#
#                                         012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations


def main():
    word = '0123456789'
    for count, item in enumerate(permutations(word, 10), 1):
        print "Index: %s of %s" % (count, ''.join(item))
        if count >= 10**6:
            break


if __name__ == '__main__':
    main()
