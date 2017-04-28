# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem22.py
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
#                                                         Names scores
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
# over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

ALPHABETICAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def score(name):
    result = 0
    for letter in name:
        index = ALPHABETICAL.index(letter)
        result += index + 1
    return result


def main():
    result = 0
    with open('p022_names.txt', 'r') as names:
        names = sorted(names.read().replace('"', '').split(','))
        for index, name in enumerate(names):
            result += ((index + 1) * score(name))
    print result


if __name__ == '__main__':
    main()
