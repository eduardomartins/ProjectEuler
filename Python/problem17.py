#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem17.py
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
# Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
# are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?

NUMBERS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

PLACES = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred",
    1000: "one thousand",
}


def count_places(num):
    total = -1

    while num > 0:
        num /= 10
        total += 1

    return total


def full_number(num):
    string = ''
    if num < 20:
        string = NUMBERS.get(num)
    else:
        while num > 0:
            places = count_places(num)
            rest = num % 10**places
            place = num - rest

            if num >= 100:
                string += PLACES.get(place)
                if rest > 0:
                    string += " and "
            elif num > 19 and num < 100:
                if rest > 0:
                    string += "%s-" % PLACES.get(place)
                else:
                    string += PLACES.get(place)
            elif num > 0 and num < 20:
                string += NUMBERS.get(num)
                num = 0

            num -= place
            places -= 1

    return string


def count_char():
    total = 0
    for num in xrange(1, 1001):
        string = full_number(num)
        print num, string
        total += len(string.replace(' ', '').replace('-', ''))
    print 'TOTAL', total


def main():
    count_char()


if __name__ == '__main__':
    main()
